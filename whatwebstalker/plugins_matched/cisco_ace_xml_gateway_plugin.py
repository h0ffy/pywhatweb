import sys
import os
			
class cisco_ace_xml_gateway_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "regexp" : "/^ACE XML Gateway$/" },
		]

