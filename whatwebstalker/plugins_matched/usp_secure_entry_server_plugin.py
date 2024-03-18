import sys
import os
			
class Pluginusp_secure_entry_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Secure Entry Server$/" },
		]

