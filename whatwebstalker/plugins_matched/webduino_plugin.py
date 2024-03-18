import sys
import os
			
class webduino_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Webduino$/ }
			{ "search" : 'headers[server]", "version" : '/^Webduino\/([^\s]+)/ }
		]

