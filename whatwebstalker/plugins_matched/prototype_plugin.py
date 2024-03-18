import sys
import os
			
class prototype_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'js tag", "regexp" : '/<script [^>]*(prototype[^>]*.js)[^>]*}
		]

