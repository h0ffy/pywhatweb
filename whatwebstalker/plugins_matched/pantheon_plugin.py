import sys
import os
			
class Pluginpantheon_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-pantheon-edge-server]", "string" : /^(.*)$/" },
			{ "search" : "headers", "regexp" : "/HTTP\/1\.[01] 404 Unknown site\!/" },
		]
		return(self.rules)

