import sys
import os
			
class dublin_core_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'dublin core", "regexp" : '/<meta [^>]*name="DC\.title"[^>]*>/i}
	]

