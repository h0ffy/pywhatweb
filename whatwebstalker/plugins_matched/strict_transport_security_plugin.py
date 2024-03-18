import sys
import os
			
class strict_transport_security_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[Strict-Transport-Security]", "string" : /^(.*)$/ }
		]

