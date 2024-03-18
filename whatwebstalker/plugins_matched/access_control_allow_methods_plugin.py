import sys
import os
			
class Pluginaccess_control_allow_methods_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[access-control-allow-methods]", "string" : /(.+)/" },
		]

