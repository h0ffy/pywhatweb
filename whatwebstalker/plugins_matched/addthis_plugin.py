import sys
import os
			
class addthis_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script [^>]*src=["|'][^>]*addthis\.com\/js/i }
		]

