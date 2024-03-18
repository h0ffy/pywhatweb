import sys
import os
			
class Plugintypepad_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="http://www.typepad.com/"'},
		]

