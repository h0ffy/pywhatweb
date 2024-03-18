import sys
import os
			
class wildcat_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^[wW]ildcat\/v([^\s]+)/ },
			{ "search" : 'headers[x-powered-by]", "version" : '/Wildcat.Net v([^\s]+)/ },
		]

