import sys
import os
			
class Plugintypekit_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["'][^>]*use\.typekit\.com/i },
		]
		return(self.rules)

