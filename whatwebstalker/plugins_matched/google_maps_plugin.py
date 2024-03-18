import sys
import os
			
class Plugingoogle_maps_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["'][^>]*maps\.google\.com\/maps(\?file=api|\/api\/staticmap)/i },
		]
		return(self.rules)

