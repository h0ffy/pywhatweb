import sys
import os
			
class stronghold_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "regexp" : "/^Stronghold$/" },
			{ "search" : "headers[server]", "version" : "/^Stronghold\/([^\s]+)/" },
			{ "search" : "headers[server]", "string" : /(C2Net[A-Z]{2}\/[^\s]+)/" },
		]

