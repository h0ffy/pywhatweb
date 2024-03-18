import sys
import os
			
class Pluginwstool_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/sourceforge\.net\/projects\/wstool" target="_blank">Server Error & SQL Injection Sacnner \(Ver ([^\s^\)]+)\)<\/a>/" },
			{ "version" : "/<title>Server Error & SQL Injection Sacnner \(Ver ([^\s^\)]+)\)<\/title>/" },
		]

