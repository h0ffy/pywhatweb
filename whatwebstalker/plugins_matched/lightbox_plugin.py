import sys
import os
			
class lightbox_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script [^>]*(lightbox[^>]*.js)[^>]*}
	]
