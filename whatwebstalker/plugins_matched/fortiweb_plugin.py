import sys
import os
			
class fortiweb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "regexp" : "/^FortiWeb$/" },
			{ "search" : "headers[server]", "version" : "/^FortiWeb-([\d\.]+)$/" },
		]

