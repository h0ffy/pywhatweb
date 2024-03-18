import sys
import os
			
class Pluginvcalendar_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.vcalendar.org">VCalendar</a>" },
			{ "certainty" : "75", "text" : "<link href="Styles/Basic/Style.css" type="text/css" rel="stylesheet"></head>" },
		]
		return(self.rules)

