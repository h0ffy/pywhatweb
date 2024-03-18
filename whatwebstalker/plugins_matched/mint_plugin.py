import sys
import os
			
class Pluginmint_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["'][^>]*mint\/\?js/i },
		]
		return(self.rules)

