import sys
import os
			
class Pluginmsgs_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<title> Mercury Satellite Ground Station: Version ([\d\.]+)<\/title>/" },
		]

