import sys
import os
			
class script_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<script(\s|>)/i },
			{ "string" : /<script[^>]+(language|type)\s*=\s*['"]?([^'"\s]+)['"]?/", "offset" : "1 },
		]

