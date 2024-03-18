import sys
import os
			
class Pluginphpmybible_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<div class='randomverse'>" },
			{ "text" : "<div class='fleft'><div class='chaphead'>" },
		]

