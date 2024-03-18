import sys
import os
			
class zeus_web_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Zeus$/ },
			{ "search" : 'headers[server]", "version" : '/^Zeus\/(([\d]+)(\.|_)([\d]+))$/ },
		]

