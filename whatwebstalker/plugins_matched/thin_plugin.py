import sys
import os
			
class thin_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^thin ([^\s]+) codename (.+)$/ }
			{ "search" : 'headers[server]", "string" : /^thin [^\s]+ (codename .+)$/ }
		]

