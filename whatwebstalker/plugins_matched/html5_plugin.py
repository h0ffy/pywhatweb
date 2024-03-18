import sys
import os
			
class Pluginhtml5_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<!DOCTYPE html>/i },
			{ "string" : "applicationCache", "regexp" : "/<html[^>]* manifest=/" },
		]
		return(self.rules)

