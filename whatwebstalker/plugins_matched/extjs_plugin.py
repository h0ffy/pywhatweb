import sys
import os
			
class extjs_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script [^>]*src=["'][^>]*ext\-base\.js["']/i }
	]

