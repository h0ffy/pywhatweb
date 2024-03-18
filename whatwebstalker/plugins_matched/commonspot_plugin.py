import sys
import os
			
class commonspot_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<meta[^>]+name="Generator"[^>]+content="CommonSpot[^"]+"[^>]*\/>/ }
			{ "regexp" : '/<img[^>]+src="[^"]+commonspot[^"]+"[^>]*\/>/ }
			{ "regexp" : '/<link[^>]+href="[^"]commonspot\/commonspot\.css"[^>]+\/>/ }
			{ "version" : '/<meta[^>]+name="Generator"[^>]+content="CommonSpot[^\d^"]+([\d\.]+)"[^>]*\/>/ }
	]

