import sys
import os
			
class Pluginmeta_powered_by_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "string" : /<meta[^>]+name=["']powered[\- ]?by["'][^>]+content=["']([^"]+)["']/i },
		]

