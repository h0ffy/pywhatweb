import sys
import os
			
class xeneo_web_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Xeneo\/([^\s]+)$/ },
			{ "search" : 'headers[server]", "regexp" : '/^Xeneo$/ },
		]

