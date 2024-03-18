import sys
import os
			
class Pluginscriptaculous_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*(scriptaculous[^>]*.js)[^>]*},
		]

