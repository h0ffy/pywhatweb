import sys
import os
			
class wanem_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<html><body><h1>WANem v([^\s^:]+): It works\!<\/h1><\/body><\/html>/ }
			{ "url" : '/WANem/about.html", "version" : '/<b>WANem v([^\s^<]+)<\/b><br>/ }
			{ "url" : '/WANem/title.html", "text" : '<TITLE>Welcome to WANem</TITLE>' }
	]

