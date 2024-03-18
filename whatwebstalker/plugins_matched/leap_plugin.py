import sys
import os
			
class Pluginleap_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="Generator" content="LEAP ([\d\.]+)"( \/)?>/" },
			{ "version" : "/<meta name="Formatter" content="LEAP ([\d\.]+)"( \/)?>/" },
		]
		return(self.rules)

