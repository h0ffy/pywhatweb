import sys
import os
			
class quantcast_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'quant.js", "regexp" : '/<script[^>]+src=["']http:\/\/edge.quantserve.com\/quant.js["']/ }
		]

