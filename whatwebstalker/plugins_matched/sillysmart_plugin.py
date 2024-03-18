import sys
import os
			
class Pluginsillysmart_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "85", "text" : "var slsBuild" },
		]
		return(self.rules)

