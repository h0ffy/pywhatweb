import plugins


class Plugincalendarscript_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75",
     "ghdb": "inurl:calendar_admin.pl intitle:Calendar Administration : Login"},
			{"certainty": "75", "ghdb": "powered by CalendarScript inurl:calendar.pl filetype:pl"},
			{"text": "<HEAD><TITLE>Calendar Administration : Login</TITLE>"},
			{"filepath": "/<FONT COLOR="red">CGISession: Session file \\[([^\\]]+)\\] could not be opened for writing!<BR><\\/FONT>/"},
			{"text": "<FONT color="  # FFFFFF" SIZE="-1">Powered by <A HREF="http://www.CalendarScript.com/" STYLE="color:#FFFFFF;">CalendarScript</A></FONT>" },
			{"text": "Powered by <A HREF="http: // www.CalendarScript.com / " CLASS="footertext" STYLE="text - decoration: underline; ">CalendarScript</A>"},
		]
	return (self.rules)
