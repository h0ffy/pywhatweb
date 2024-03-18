import sys
import os
			
class cern_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^CERN\/([^\s]+)/ }
		]

