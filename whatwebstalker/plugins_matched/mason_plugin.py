import sys
import os
			
class Pluginmason_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-powered-by]", "regexp" : "/HTML::Mason/" },
		]
		return(self.rules)

