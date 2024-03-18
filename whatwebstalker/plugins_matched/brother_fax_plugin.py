import sys
import os
			
class Pluginbrother_fax_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "model" : "/<TITLE>\nBrother (MFC-[\dA-Z]+)\n<\/TITLE>/" },
			{ "certainty" : "25", "search" : "headers[server]", "version" : "/^[Dd]ebut\/([\d\.]+)$/" },
		]

