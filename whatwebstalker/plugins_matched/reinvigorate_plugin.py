import sys
import os
			
class reinvigorate_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "10", "text" : "<!-- Reinvigorate -->" },
			{ "text" : "<script type="text/javascript" src="http://include.reinvigorate.net/re_.js"></script>" },
			{ "certainty" : "25", "string" : /reinvigorate\.track\("([a-z\d]{5}-[a-z\d]{10})"\);/" },
			{ "certainty" : "10", "string" : /re_\("([a-z\d]{5}-[a-z\d]{10})"\);/" },
		]

