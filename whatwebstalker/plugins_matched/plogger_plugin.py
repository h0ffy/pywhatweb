import sys
import os
			
class plogger_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<title>[^powered]+powered by Plogger Gallery<\/title>/" },
			{ "regexp" : "/<a[\ title="Powered by Plogger"]* href="http:\/\/www.plogger.org\/">Powered by Plogger[!]*<\/a>/" },
		]

