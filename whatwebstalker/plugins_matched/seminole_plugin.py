import sys
import os
			
class seminole_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "version" : "/^Seminole\/([^\s]+)/" },
		]

