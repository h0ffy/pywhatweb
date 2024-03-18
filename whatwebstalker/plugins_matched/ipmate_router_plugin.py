import sys
import os
			
class Pluginipmate_router_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<TITLE>Welcome to IPMATE</TITLE>" },
			{ "url" : "/images/ipmate_logo.gif", "md5" : "8d16375ac9c6c0fc1c27c0183dfda573" },
		]

