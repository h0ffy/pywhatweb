import sys
import os
			
class Plugincisco_ace_xml_gateway_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^ACE XML Gateway$/" },
		]
		return(self.rules)

