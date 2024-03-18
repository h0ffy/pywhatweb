import sys
import os
			
class Plugintcms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "powered by TCMS"", "certainty" : "75 },
		]
		return(self.rules)

