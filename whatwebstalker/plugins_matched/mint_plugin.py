import sys
import os
			
class mint_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<script [^>]*src=["'][^>]*mint\/\?js/i },
		]

