import sys
import os
			
class modernizr_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script [^>]*src=["'][^>]*modernizr[^>]*\.js/i },
			{ "version" : '/<script [^>]*src=["'][^>]*modernizr-([^>]+)\.js/i },
		]

