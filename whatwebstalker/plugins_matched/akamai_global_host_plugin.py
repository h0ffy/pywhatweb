import sys
import os
			
class Pluginakamai_global_host_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^AkamaiGHost/" },
		]

