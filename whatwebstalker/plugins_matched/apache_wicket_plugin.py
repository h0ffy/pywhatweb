import sys
import os
			
class Pluginapache_wicket_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "inurl:"wicket:bookmarkablePage=:"" },
		]
		return(self.rules)

