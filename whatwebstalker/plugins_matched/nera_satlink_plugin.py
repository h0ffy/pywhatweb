import sys
import os
			
class Pluginnera_satlink_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[www-authenticate]", "regexp" : "/^Basic realm="SatLink Terminal"$/" },
		]
		return(self.rules)

