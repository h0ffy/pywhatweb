import sys
import os
			
class mark_of_the_web_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<!-- saved from url=\([\d]+\)([^>]+) -->[\r\n]/ },
		]

