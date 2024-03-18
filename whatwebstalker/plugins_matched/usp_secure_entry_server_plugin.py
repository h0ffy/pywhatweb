import sys
import os
			
class Pluginusp_secure_entry_server_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Secure Entry Server$/" },
		]
		return(self.rules)

