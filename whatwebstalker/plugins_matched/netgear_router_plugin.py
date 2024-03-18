import sys
import os
			
class netgear_router_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/^Basic realm="?[\s]*Netgear/", "certainty" : '75", "search" : 'headers[www-authenticate]" }
			{ "model" : '/^Basic realm="?[\s]*NETGEAR ([^"]+)[\s]*"?/", "certainty" : '75", "search" : 'headers[www-authenticate]" }
	]

