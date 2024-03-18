import sys
import os
			
class Plugincern_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^CERN\/([^\s]+)/" },
		]

