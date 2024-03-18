import sys
import os
			
class Plugincomanche_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Comanche\/([^\s]+)/" },
		]
		return(self.rules)

