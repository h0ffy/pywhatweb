import sys
import os
			
class Pluginkinja_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "X-Kinja Header", "regexp" : "/^$/", "search" : "headers[x-kinja]" },
		]
		return(self.rules)

