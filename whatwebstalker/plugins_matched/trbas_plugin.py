import sys
import os
			
class Plugintrbas_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" :  '<link rel="stylesheet" href="http://www.trbas.com" },
		]
		return(self.rules)

