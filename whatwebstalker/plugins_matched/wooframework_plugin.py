import sys
import os
			
class Pluginwooframework_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="WooFramework ([\d\.]+)"/" },
		]
		return(self.rules)

