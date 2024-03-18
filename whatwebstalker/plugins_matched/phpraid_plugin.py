import sys
import os
			
class phpraid_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "text" : 'Raid Management Provided by phpRaid' },
			{ "version" : '/Raid Management Provided by <a href="http:\/\/www.spiffyjr.com\/">phpRaid<\/a> v([\d\.]+)/ },
		]

