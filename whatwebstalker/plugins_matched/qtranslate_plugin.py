import sys
import os
			
class Pluginqtranslate_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/qtrans_cookie_test=[^\+]+\+Cookie\+Test;/" },
		]
		return(self.rules)

