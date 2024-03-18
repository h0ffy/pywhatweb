import sys
import os
			
class Pluginsocorro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://code.google.com/p/socorro/">Socorro</a>" },
		]

