import sys
import os
			
class webbler_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="generator" content="webbler ([^\s]+) - http:\/\/tincan\.co\.uk\/webbler"  \/?>/ },
		]

