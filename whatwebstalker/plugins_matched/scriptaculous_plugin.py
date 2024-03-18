import sys
import os
			
class Pluginscriptaculous_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*(scriptaculous[^>]*.js)[^>]*},
		]
		return(self.rules)

