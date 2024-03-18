import sys
import os
			
class roxen_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Roxen$/ }
			{ "search" : 'headers[server]", "version" : '/^Roxen\/([^\s]+)$/ }
		]

