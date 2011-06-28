#------------------------------Standard import-------------------------------------#
import webnotes
import smtplib
#import datetime
import re
from webnotes.utils import add_days, add_months, add_years, cint, cstr, date_diff, default_fields, flt, fmt_money, formatdate, generate_hash, getTraceback, get_defaults, get_first_day, get_last_day, getdate, has_common, month_name, now, nowdate, replace_newlines, sendmail, set_default, str_esc_quote, user_format, validate_email_add
from webnotes.model import db_exists
from webnotes.model.doc import Document, addchild, removechild, getchildren, make_autoname, SuperDocType
from webnotes.model.doclist import getlist, copy_doclist
from webnotes.model.code import get_obj, get_server_obj, run_server_obj, updatedb, check_syntax
from webnotes import session, form, is_testing, msgprint, errprint
from datetime import datetime
set = webnotes.conn.set
sql = webnotes.conn.sql
get_value = webnotes.conn.get_value
in_transaction = webnotes.conn.in_transaction
convert_to_lists = webnotes.conn.convert_to_lists
#---------------------------------------------------------------------------------#
def send_mail1(self):
	from1='internatrails@gmail.com'
	to=self.doc.email
	subject="Confirmation of your event registration in wnframework"
	headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" %(from1,to,subject)
	message = headers +" Thanks for registering! Here are your registration details \n"+"Event Name : "+self.doc.event_name+"\nRegistrant Name: "+self.doc.name1+"\n Phone number: "+self.doc.phone+"\n Address: "+self.doc.address
	mailserver = smtplib.SMTP('smtp.gmail.com')
	#if debug == 1: mailserver.set_debuglevel(1)
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	#Define username / password if using SMTP Auth
	username = 'internatrails@gmail.com'
	#password = getpass.getpass("%s's password: " % username)
	mailserver.login(username,'mambalam')
	mailserver.sendmail(from1, to, message)
	mailserver.close()
	msgprint("Mail has been sent to "+self.doc.email)

def validateEmail(email):
		if len(email) > 7:
			if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
				return 1
		return 0

def validatePhone(phone):
		flag=0
		if len(phone) == 10:
			for i in phone:
				if i.isdigit():
					flag+=1
			if flag==10:
				return 1
			else:
				return 0
		else:
			return 0
		

class DocType:

   #standard constructor
	def __init__(self, doc, doclist):
		self.doc = doc
		self.doclist = doclist


	def set_fields(self,fieldName):
		#msgprint("hi")
                if fieldName!='no_of_attendees':
			field1=sql("select "+fieldName+" from `tabEvent Creation` where event_name = %s", self.doc.event_name)
		if fieldName=='event_date':
            		ret = { fieldName : str(field1[0][0]) }
            		return str(ret)   
		elif fieldName=='no_of_attendees':
			att=sql("select seats_filled from `tabEvent Creation` where event_name = %s",self.doc.event_name)
			ret = { fieldName : att[0][0] }			
			return str(ret)
		else:
			ret = { fieldName : field1[0][0] }
                        return str(ret)
     
   
	def confirm_reg(self):
		if validateEmail(self.doc.email)!=1:
			msgprint("Enter proper Email")
			raise Exception
		if validatePhone(self.doc.phone)!=1:
			msgprint("Enter proper Phone number")
			raise Exception
		count=sql("select seats_filled from `tabEvent Creation` where event_name = %s",self.doc.event_name)
                maxCount=sql("select maximum_seats from `tabEvent Creation` where event_name=%s",self.doc.event_name)
                if count[0][0]>=maxCount[0][0]:
			msgprint("Sorry! The seats are full")
                        raise Exception
		else:
			incre=int(count[0][0])+1
                        sql("update `tabEvent Creation` set seats_filled="+str(incre)+" where event_name = %s",self.doc.event_name)
                        msgprint("Congrats! You have successfully registered for the event")

	def ret_val(self,fname):
		fval=self.doc.fname
		msgprint(fval)
		
	def send_mail(self):
		msgprint(self.doc.event_name)
		msgprint(self.doc.event_type)
		send_mail1(self);

	
