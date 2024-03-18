import sys
import os
			
class Pluginpowerschool_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^PowerSchool$/" },
		]
		return(self.rules)

