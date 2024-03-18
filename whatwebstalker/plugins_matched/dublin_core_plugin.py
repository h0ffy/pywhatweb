import sys
import os
			
class Plugindublin_core_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "dublin core", "regexp" : "/<meta [^>]*name="DC\.title"[^>]*>/i},
		]
		return(self.rules)

