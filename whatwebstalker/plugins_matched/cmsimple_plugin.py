import sys
import os
			
class Plugincmsimple_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "ghdb" : "Powered by CMSimple.dk" welcome", "certainty" : "75 },
			{ "text" : "<meta name="generator" content="CMSimple" },
			{ "version" : "/<meta name="generator" content="CMSimple ([\d\.]+)[^>]*>/" },
		]

