import sys
import os
			
class nera_satlink_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[www-authenticate]", "regexp" : '/^Basic realm="SatLink Terminal"$/ },
		]

