import sys
import os
			
class Pluginiciniti_store_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- START (content_stylesheet.inc) -->" },
		]
		return(self.rules)

