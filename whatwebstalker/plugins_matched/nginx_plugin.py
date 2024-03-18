import sys
import os
			
class nginx_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^nginx$/ },
			{ "search" : 'headers[server]", "version" : '/^nginx\/([^\s]+).*$/ },
		]

