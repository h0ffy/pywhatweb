import sys
import os
			
class xybershield_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[set-cookie]", "regexp" : '/XyberShieldSession=[^\s]+;/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/XyberShieldStatus=[^\s]+;/ }
	]

