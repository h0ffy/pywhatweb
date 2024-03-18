import sys
import os
			
class Pluginxitami_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Xitami$/" },
			{ "search" : "headers[server]", "version" : "/^Xitami\/([^\s]+)$/" },
		]

