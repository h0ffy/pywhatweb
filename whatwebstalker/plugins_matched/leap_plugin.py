import sys
import os
			
class leap_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="Generator" content="LEAP ([\d\.]+)"( \/)?>/ },
			{ "version" : '/<meta name="Formatter" content="LEAP ([\d\.]+)"( \/)?>/ },
		]

