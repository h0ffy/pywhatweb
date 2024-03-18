import sys
import os
			
class ibm_webseal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^WebSEAL\/([^\s]+ \(Build \d+\))/ }
		]

