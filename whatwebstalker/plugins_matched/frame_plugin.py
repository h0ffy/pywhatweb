import sys
import os
			
class Pluginframe_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<i?frame\s+/i },
		]
		return(self.rules)

