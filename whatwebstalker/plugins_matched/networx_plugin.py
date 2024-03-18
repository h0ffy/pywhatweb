import sys
import os
			
class Pluginnetworx_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.socialabc.com">NetworX</a>" },
		]
		return(self.rules)

