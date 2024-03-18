import sys
import os
			
class html5_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<!DOCTYPE html>/i }
			{ "string" : 'applicationCache", "regexp" : '/<html[^>]* manifest=/ }
		]

