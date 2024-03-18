import sys
import os
			
class raidenhttpd_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "version" : "/^RaidenHTTPD\/([^\s]+) \([^\)]+\)$/" },
			{ "search" : "headers[server]", "string" : /^RaidenHTTPD\/[^\s]+ \(([^\)]+)\)$/" },
		]

