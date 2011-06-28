
function EnterData(etype,eduration,edate,evenue,noatt)
{
		doc.event_type='<html><body><b>'+etype+'</b></body></html>';
		unhide_field(['event_type','event_duration','reg_date','event_date','sec_break','event_venue','sec_break2','no_of_attendees','reg_button']);
		doc.event_duration='<html><body><b>'+eduration+'</b></body></html>';
		doc.event_venue='<html><body><b>'+evenue+'</b></body></html>';
		doc.event_date=edate;
		doc.no_of_attendees=noatt;
		refresh_field('event_type');
		refresh_field('event_duration');
		refresh_field('event_date');
		refresh_field('event_venue');
		refresh_field('no_of_attendees');
		refresh_field('sec_break');
		refresh_field('sec_break2');
	//--------Manipulating with Date variables----------

	var currentDate = new Date();
	var dat=currentDate.getDate();
	var mon=currentDate.getMonth()+1;
	var year=currentDate.getFullYear();
		if(dat<10)
		dat="0"+dat;
		if(mon<10)
		mon="0"+mon;
	var sysDate=year+"-"+mon+"-"+dat;
        var eventDate=doc.event_date;

	if(sysDate>eventDate)
	{
		
		sysDate=dat+"-"+mon+"-"+year;
		alert("Sorry! The Event is Over!");		
		doc.reg_date=sysDate;
		refresh_field('reg_date');
	}
	else
	{			
		sysDate=dat+"-"+mon+"-"+year;		
		doc.reg_date=sysDate;
		refresh_field('reg_date');
	}

	
}
cur_frm.cscript.event_name=function(doc,cdt,cdn){
	
	

	if(doc.event_name=='Event A')
		{EnterData("Education","4 hrs","2008-09-08","Chennai",400);
		//get_server_fields('get_noatt', '', '', doc, cdt, cdn, 1);
		}
	if(doc.event_name=='Event B')
		EnterData("Entertainment","7.5 hrs","2011-09-08","Hyderabad",300);
	if(doc.event_name=='Event C')
		EnterData("Technical","3.5 hrs","2011-06-03","Mumbai",210);
	if(doc.event_name=='Event D')
		EnterData("Comedy","6 hrs","2011-09-08","Australia",100);
	if(doc.event_name=='Event E')
		EnterData("Motivation","4 hrs","2011-11-28","Delhi",101);
	if(doc.event_name=='SELECT EVENT')
		hide_field(['event_type','event_duration','reg_date','event_date','sec_break','event_venue','sec_break2','no_of_attendees','reg_button']);
	}

		
		
		
		
		

		

