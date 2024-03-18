import sys
import os
			
class Pluginbackbee_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "100", "text" : "<div id="bb5-site-wrapper">" },
		]
		return(self.rules)

