import sys
import os
			
class winstone_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Winstone Servlet Engine v([^\s]+)/ },
			{ "search" : 'headers[x-powered-by]", "version" : '/Servlet\/[^\s]+ \(Winstone\/([^\)]+)\)/ },
		]

