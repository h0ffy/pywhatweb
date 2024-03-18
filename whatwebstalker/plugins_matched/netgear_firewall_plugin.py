import sys
import os
			
class netgear_firewall_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "regexp" : "/^NETGEAR Firewall$/" },
		]

