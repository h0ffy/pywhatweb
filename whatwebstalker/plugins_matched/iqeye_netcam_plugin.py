import sys
import os
			
class Pluginiqeye_netcam_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "model" : "/<title>IQeye([^:]+): Live Images[^<]*<\/title>/i },
		]

