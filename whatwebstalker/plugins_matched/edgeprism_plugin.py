import sys
import os
			
class Pluginedgeprism_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^EdgePrism\/([^\s]+)$/" },
			{ "search" : "headers[server]", "regexp" : "/^EdgePrismSSL/" },
		]
		return(self.rules)

