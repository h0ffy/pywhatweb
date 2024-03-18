import sys
import os
			
class Pluginquickweb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<HTML><HEAD><TITLE>QWScript Error</TITLE></HEAD>" },
		]

