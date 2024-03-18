import sys
import os
			
class filevista_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<!--\r?\n\tFileVista v([\d\.]+)\r?\n\tCopyright /" },
			{ "text" : "<td>Welcome to FileVista<br />Please enter your credentials:</td>" },
		]

