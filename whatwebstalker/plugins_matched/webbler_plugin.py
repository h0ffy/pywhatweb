import sys
import os
			
class Pluginwebbler_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="webbler ([^\s]+) - http:\/\/tincan\.co\.uk\/webbler"  \/?>/" },
		]
		return(self.rules)

