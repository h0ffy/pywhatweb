import sys
import os
			
class edgeprism_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^EdgePrism\/([^\s]+)$/ },
			{ "search" : 'headers[server]", "regexp" : '/^EdgePrismSSL/ },
		]

