import sys
import os
			
class Pluginibm_websphere_datapower_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-backside-transport]", "string" : /(FAIL|OK)/" },
		]
		return(self.rules)

