import sys
import os
			
class hp_system_management_homepage_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "regexp" : '/<TITLE>HP System Management Homepage Login<\/TITLE>/ },
			{ "search" : 'headers[set-cookie]", "regexp" : '/Compaq-HMMD=/ },
			{ "search" : 'headers[server]", "version" : '/CompaqHTTPServer\/[^\s]+ HP System Management Homepage\/([\d\.]+)$/ },
		]

