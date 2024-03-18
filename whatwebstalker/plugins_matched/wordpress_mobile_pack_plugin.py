import sys
import os
			
class Pluginwordpress_mobile_pack_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-mobilized-by]", "version" : "/^WordPress Mobile Pack ([^\s]+)$/" },
		]
		return(self.rules)

