import sys
import os
			
class hikvision_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Hikvision-Webs$/ }
	]

