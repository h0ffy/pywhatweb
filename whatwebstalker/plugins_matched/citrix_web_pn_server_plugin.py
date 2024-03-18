import sys
import os
			
class citrix_web_pn_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Citrix Web PN Server$/ }
		]

