import sys
import os
			
class intrinsyc_deviceweb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Intrinsyc deviceWEB v([\d\.]+)$/ }
	]

