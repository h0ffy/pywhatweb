import sys
import os
			
class google_maps_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script [^>]*src=["'][^>]*maps\.google\.com\/maps(\?file=api|\/api\/staticmap)/i }
	]

