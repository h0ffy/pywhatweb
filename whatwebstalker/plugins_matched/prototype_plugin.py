import sys
import os
			
class Pluginprototype_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "name" : "js tag", "regexp" : "/<script [^>]*(prototype[^>]*.js)[^>]*},
		]

