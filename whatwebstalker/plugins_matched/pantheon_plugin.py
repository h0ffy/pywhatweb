import sys
import os
			
class pantheon_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-pantheon-edge-server]", "string" : /^(.*)$/ },
			{ "search" : 'headers", "regexp" : '/HTTP\/1\.[01] 404 Unknown site\!/ },
		]

