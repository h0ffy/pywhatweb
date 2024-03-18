import sys
import os
			
class wpquiz_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<title>[^>]*>> [Register|Login]+ - wp[q|Q]+uiz<\/title>/ }
		]

