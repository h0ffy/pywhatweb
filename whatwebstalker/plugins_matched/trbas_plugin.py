import sys
import os
			
class Plugintrbas_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" :  '<link rel="stylesheet" href="http://www.trbas.com" },
		]

