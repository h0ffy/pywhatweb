import sys
import os
			
class akamai_global_host_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^AkamaiGHost/ }
	]

