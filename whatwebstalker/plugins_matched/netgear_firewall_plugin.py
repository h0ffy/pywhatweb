import sys
import os
			
class Pluginnetgear_firewall_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^NETGEAR Firewall$/" },
		]
		return(self.rules)

