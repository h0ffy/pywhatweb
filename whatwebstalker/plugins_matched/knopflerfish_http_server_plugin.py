import sys
import os
			
class knopflerfish_http_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^The Knopflerfish HTTP Server$/ }
		]

