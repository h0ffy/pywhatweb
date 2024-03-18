import sys
import os
			
class typekit_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script [^>]*src=["'][^>]*use\.typekit\.com/i }
		]

