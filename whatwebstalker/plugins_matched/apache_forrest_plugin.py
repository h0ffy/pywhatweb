import sys
import os
			
class apache_forrest_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta content="Apache Forrest" name="Generator"' }
			{ "version" : '/<meta content="([^"^>]+)" name="Forrest-version"/ }
			{ "version" : '/<meta name="Forrest-version" content="([^"^>]+)"/ }
			{ "module" : /<meta content="([^"^>]+)" name="Forrest-theme-name"/ }
			{ "module" : /<meta name="Forrest-theme-name" content="([^"^>]+)"/ }
			{ "module" : /<meta name="Forrest-skin-name" content="([^"^>]+)"/ }
			{ "module" : /<meta content="([^"^>]+)" name="Forrest-skin-name"/ }
	]

