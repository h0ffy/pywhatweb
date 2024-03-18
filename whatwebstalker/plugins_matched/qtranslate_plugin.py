import sys
import os
			
class qtranslate_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[set-cookie]", "regexp" : '/qtrans_cookie_test=[^\+]+\+Cookie\+Test;/ }
	]

