import sys
import os
			
class Pluginxitami_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Xitami$/" },
			{ "search" : "headers[server]", "version" : "/^Xitami\/([^\s]+)$/" },
		]
		return(self.rules)

