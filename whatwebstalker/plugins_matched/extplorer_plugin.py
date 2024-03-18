import sys
import os
			
class Pluginextplorer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "url" : "/extplorer.xml", "version" : "/<version>([^<]+)<\/version>/" },
			{ "text" : "<title>Login - eXtplorer</title>" },
		]

