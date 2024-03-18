import sys
import os
			
class Plugincern_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^CERN\/([^\s]+)/" },
		]
		return(self.rules)

