import sys
import os
			
class Pluginnera_satlink_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[www-authenticate]", "regexp" : "/^Basic realm="SatLink Terminal"$/" },
		]

