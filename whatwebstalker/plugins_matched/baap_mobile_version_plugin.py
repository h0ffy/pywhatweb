import sys
import os
			
class baap_mobile_version_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-mobilized-by]", "version" : '/^BAAP Mobile Version ([^\s]+)$/ },
		]

