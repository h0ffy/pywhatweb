import sys
import os
			
class Plugincl_http_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^CL-HTTP\/([^\s]+)/" },
			{ "search" : "headers[server]", "string" : /^CL-HTTP\/[^\s]+ \(([^\)]+)\)/" },
		]

