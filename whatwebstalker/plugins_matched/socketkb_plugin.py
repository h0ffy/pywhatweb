import sys
import os
			
class Pluginsocketkb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/>Powered by SocketKB version ([\d\.]+)<\/a>/" },
		]

