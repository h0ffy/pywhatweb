import sys
import os
			
class microsys_promotic_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Promotic$/ },
			{ "text" : '<html><head><title>PROMOTIC Redirection</title></head>' },
		]

