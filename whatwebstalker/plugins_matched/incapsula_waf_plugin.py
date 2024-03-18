import sys
import os
			
class incapsula_waf_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : "Set-cookie Header", "search" : "headers[set-cookie]", "regexp" : "/incap_ses_/i},
			{ "name" : "Set-cookie Header", "search" : "headers[set-cookie]", "regexp" : "/incap_visid_83_/i},
			{ "name" : "visid_incap_ cookie", "search" : "headers[set-cookie]", "regexp" : "/^visid_incap_/" },
		]

