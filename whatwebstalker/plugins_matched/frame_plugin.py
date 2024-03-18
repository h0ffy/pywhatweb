import sys
import os
			
class Pluginframe_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<i?frame\s+/i },
		]

