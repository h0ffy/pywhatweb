import sys
import os
			
class meta_author_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<meta[^>^=]+name[\s]*=[\s]*['"]?author['"]?[^>^=]+content[\s]*=[\s]*['"]([^'^"^>]+)/i },
			{ "string" : /<meta[^>^=]+content[\s]*=[\s]*['"]([^"^'^>]+)['"][^>^=]+name[\s]*=[\s]*['"]?author['"]?/i },
		]

