import sys
import os
			
class symantec_client_security_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- Symantec Client Security Web Based Installation -->' }
			{ "certainty" : '75", "string" : /<META NAME="Copyright" Content="Copyright (20[\d]{2}) Symantec Corporation">/ }
	]

