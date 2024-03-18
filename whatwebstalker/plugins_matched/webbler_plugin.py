import sys
import os
			
class Pluginwebbler_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="webbler ([^\s]+) - http:\/\/tincan\.co\.uk\/webbler"  \/?>/" },
		]

