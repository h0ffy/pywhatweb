import sys
import os
			
class rios_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-rbt-optimized-by]", "version" : '/\(RiOS ([^\s]+)\)/ },
			{ "search" : 'headers[x-rbt-optimized-by]", "string" : /(.+) \(RiOS/ },
		]

