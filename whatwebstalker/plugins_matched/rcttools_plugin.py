import sys
import os
			
class Pluginrcttools_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^RCTTools \(SecureSOHO Web configuration Tools\) v([^\s]+)$/" },
		]

