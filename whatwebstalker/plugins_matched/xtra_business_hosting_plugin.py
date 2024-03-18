import sys
import os
			
class Pluginxtra_business_hosting_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Xtra Business: Web Hosting</title>" },
		]
		return(self.rules)

