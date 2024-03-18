import sys
import os
			
class Pluginiciniti_store_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- START (content_stylesheet.inc) -->" },
		]

