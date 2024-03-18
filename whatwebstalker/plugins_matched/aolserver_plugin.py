import sys
import os
			
class Pluginaolserver_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^AOLserver$/" },
			{ "search" : "headers[server]", "version" : "/^AOLserver\/([^\s]+)/" },
		]
		return(self.rules)

