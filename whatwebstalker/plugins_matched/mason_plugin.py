import sys
import os
			
class mason_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[x-powered-by]", "regexp" : "/HTML::Mason/" },
		]

