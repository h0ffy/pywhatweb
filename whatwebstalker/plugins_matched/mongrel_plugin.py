import sys
import os
			
class Pluginmongrel_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Mongrel ([\d][^\s]+)/" },
		]
		return(self.rules)

