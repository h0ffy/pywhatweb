import sys
import os
			
class Pluginmsgs_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title> Mercury Satellite Ground Station: Version ([\d\.]+)<\/title>/" },
		]
		return(self.rules)

