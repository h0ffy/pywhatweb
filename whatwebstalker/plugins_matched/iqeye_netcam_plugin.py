import sys
import os
			
class Pluginiqeye_netcam_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "model" : "/<title>IQeye([^:]+): Live Images[^<]*<\/title>/i },
		]
		return(self.rules)

