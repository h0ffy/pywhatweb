import sys
import os
			
class Plugincitrix_web_pn_server_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Citrix Web PN Server$/" },
		]
		return(self.rules)

