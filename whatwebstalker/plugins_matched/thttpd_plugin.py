import sys
import os
			
class Pluginthttpd_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^thttpd\/([^\s]+)/" },
		]
		return(self.rules)

