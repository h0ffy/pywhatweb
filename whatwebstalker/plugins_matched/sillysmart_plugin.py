import sys
import os
			
class Pluginsillysmart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "85", "text" : "var slsBuild" },
		]

