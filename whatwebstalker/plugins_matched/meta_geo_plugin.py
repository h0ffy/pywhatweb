import sys
import os
			
class meta_geo_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<meta name="geo.[^"]+" content="([^"]+)"[^>]*>},
			{ "string" : /<meta name="ICBM" content="([^"]+)"[^>]*>/" },
		]

