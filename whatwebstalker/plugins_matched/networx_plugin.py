import sys
import os
			
class Pluginnetworx_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.socialabc.com">NetworX</a>" },
		]

