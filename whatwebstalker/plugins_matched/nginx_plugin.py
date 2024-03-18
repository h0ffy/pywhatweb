import sys
import os
			
class Pluginnginx_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^nginx$/" },
			{ "search" : "headers[server]", "version" : "/^nginx\/([^\s]+).*$/" },
		]
		return(self.rules)

