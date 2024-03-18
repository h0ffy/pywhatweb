import sys
import os
			
class Pluginzope_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/Zope\/\(([^,]*)/" },
			{ "search" : "headers[server]", "module" : /Zope\/\([^,]*", "([^,]*)/" },
			{ "search" : "headers[server]", "string" : /Zope\/\([^,]*", "[^,]*", "([^\)^\s]*)/" },
		]

