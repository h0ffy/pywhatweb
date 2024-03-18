import sys
import os
			
class siemens_router_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[www-authenticate]", "model" : '/Basic realm="Siemens ADSL ([^"^\s]+)"/", "certainty" : '75 }
		]

