import sys
import os
			
class fluentnet_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'powered by FluentCMS from DotContent"", "certainty" : '75 }
			{ "version" : '/<meta name="GENERATOR" content="Fluent[CMS|NET]+ ([\d\.]+) / }
	]

