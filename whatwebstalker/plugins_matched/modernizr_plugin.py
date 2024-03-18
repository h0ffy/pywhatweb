import sys
import os
			
class Pluginmodernizr_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["'][^>]*modernizr[^>]*\.js/i },
			{ "version" : "/<script [^>]*src=["'][^>]*modernizr-([^>]+)\.js/i },
		]
		return(self.rules)

