import sys
import os
			
class Plugintcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "ghdb" : "powered by TCMS"", "certainty" : "75 },
		]

