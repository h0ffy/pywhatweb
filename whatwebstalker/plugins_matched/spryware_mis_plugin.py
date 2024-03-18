import sys
import os
			
class spryware_mis_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "version" : "/^SpryWare\/([^\s]+)$/" },
			{ "search" : "headers[x-deprecated-response]", "regexp" : "/^Invalid CheckSum Received$/" },
		]

