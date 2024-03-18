import sys
import os
			
class Pluginkinja_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "name" : "X-Kinja Header", "regexp" : "/^$/", "search" : "headers[x-kinja]" },
		]

