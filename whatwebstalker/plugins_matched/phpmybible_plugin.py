import sys
import os
			
class Pluginphpmybible_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div class='randomverse'>" },
			{ "text" : "<div class='fleft'><div class='chaphead'>" },
		]
		return(self.rules)

