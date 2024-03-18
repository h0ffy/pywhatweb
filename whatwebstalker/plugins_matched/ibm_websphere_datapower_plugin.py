import sys
import os
			
class Pluginibm_websphere_datapower_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[x-backside-transport]", "string" : /(FAIL|OK)/" },
		]

