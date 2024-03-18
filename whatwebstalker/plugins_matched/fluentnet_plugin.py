import sys
import os
			
class Pluginfluentnet_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "powered by FluentCMS from DotContent"", "certainty" : "75 },
			{ "version" : "/<meta name="GENERATOR" content="Fluent[CMS|NET]+ ([\d\.]+) /" },
		]
		return(self.rules)

