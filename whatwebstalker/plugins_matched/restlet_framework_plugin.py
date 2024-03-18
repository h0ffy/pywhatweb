import sys
import os
			
class Pluginrestlet_framework_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Restlet-Framework\/([^\s]+)$/" },
		]
		return(self.rules)

