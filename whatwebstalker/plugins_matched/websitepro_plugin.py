import sys
import os
			
class websitepro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^WebSitePro\/([^\s]+)/ }
	]

