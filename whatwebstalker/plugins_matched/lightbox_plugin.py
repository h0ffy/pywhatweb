import sys
import os
			
class Pluginlightbox_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*(lightbox[^>]*.js)[^>]*},
		]
		return(self.rules)

