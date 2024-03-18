import sys
import os
			
class msgs_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<title> Mercury Satellite Ground Station: Version ([\d\.]+)<\/title>/ }
	]

