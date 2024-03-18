import sys
import os
			
class wordpress_mobile_pack_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[x-mobilized-by]", "version" : "/^WordPress Mobile Pack ([^\s]+)$/" },
		]

