import sys
import os
			
class wooframework_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="generator" content="WooFramework ([\d\.]+)"/ }
		]

