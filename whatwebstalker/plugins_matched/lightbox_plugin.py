import sys
import os
			
class Pluginlightbox_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*(lightbox[^>]*.js)[^>]*},
		]

