import sys
import os
			
class Pluginapache_wicket_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "ghdb" : "inurl:"wicket:bookmarkablePage=:"" },
		]

