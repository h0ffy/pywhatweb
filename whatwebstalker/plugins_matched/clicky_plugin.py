import sys
import os
			
class clicky_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script[^>]+src=["'](https?:)?\/\/static\.getclicky\.com/i }
	]

