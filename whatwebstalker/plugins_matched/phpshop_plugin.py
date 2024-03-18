import sys
import os
			
class phpshop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "regexp" : '/Powered by phpShop/i },
			{ "regexp" : '/Powered by <a href="http:\/\/www.phpshop.org"[^>]*>phpShop<\/a>/i },
			{ "version" : '/Powered by <a href="http:\/\/www.phpshop.org"[^>]*>phpShop<\/a>[\r\n\s]+([\d\.]+) / },
		]

