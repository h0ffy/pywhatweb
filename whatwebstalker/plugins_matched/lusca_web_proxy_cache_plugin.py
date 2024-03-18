import sys
import os
			
class lusca_web_proxy_cache_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Lusca$/ }
			{ "search" : 'headers[server]", "version" : '/^Lusca\/LUSCA_HEAD-([^\s]+)$/ }
		]

