import sys
import os
			
class laserwash_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "status" : '401", "search" : 'headers[www-authenticate]", "regexp" : '/^Basic realm="PDQ Laserwash"$/ }
	]

