import sys
import os
			
class Pluginsharethis_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["|'][^"^']+w\.sharethis\.com\//i },
		]

