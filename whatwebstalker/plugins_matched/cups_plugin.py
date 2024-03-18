import sys
import os
			
class cups_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "version" : "/^CUPS\/([^\s]+)$/" },
			{ "search" : "headers[upgrade]", "regexp" : "/^TLS\/1\.0,HTTP\/1\.1$/", "certainty" : "25 },
		]

