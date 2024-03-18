import sys
import os
			
class Plugincl_http_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^CL-HTTP\/([^\s]+)/" },
			{ "search" : "headers[server]", "string" : /^CL-HTTP\/[^\s]+ \(([^\)]+)\)/" },
		]
		return(self.rules)

