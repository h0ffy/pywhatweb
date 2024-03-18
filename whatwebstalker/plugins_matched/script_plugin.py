import sys
import os
			
class Pluginscript_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script(\s|>)/i },
			{ "string" : /<script[^>]+(language|type)\s*=\s*['"]?([^'"\s]+)['"]?/", "offset" : "1 },
		]
		return(self.rules)

