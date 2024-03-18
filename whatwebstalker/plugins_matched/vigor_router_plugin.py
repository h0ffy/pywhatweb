import sys
import os
			
class vigor_router_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "model" : '/^(VigorAccess) Web Server$/ }
			{ "search" : 'headers[www-authenticate]", "model" : '/^Basic realm="(Login to )?Vigor ([\d]+)"$/", "offset" : '1 }
		]

