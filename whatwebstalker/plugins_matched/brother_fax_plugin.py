import sys
import os
			
class Pluginbrother_fax_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "model" : "/<TITLE>\nBrother (MFC-[\dA-Z]+)\n<\/TITLE>/" },
			{ "certainty" : "25", "search" : "headers[server]", "version" : "/^[Dd]ebut\/([\d\.]+)$/" },
		]
		return(self.rules)

