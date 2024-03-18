import sys
import os
			
class content_security_policy_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-content-security-policy]", "string" : /^(.*)$/ }
			{ "search" : 'headers[x-webkit-csp]", "string" : /^(.*)$/ }
	]

