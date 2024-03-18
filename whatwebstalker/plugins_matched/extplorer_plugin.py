import sys
import os
			
class Pluginextplorer_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/extplorer.xml", "version" : "/<version>([^<]+)<\/version>/" },
			{ "text" : "<title>Login - eXtplorer</title>" },
		]
		return(self.rules)

