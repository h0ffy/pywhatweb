import sys
import os
			
class informatics_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[set-cookie]", "regexp" : '/[\d]+=HTMLTitle=[^\s]*&OrgName=[^\s]+&EmailThankYou=[^\s]*&DefaultIdPage=[^\s]+&State=/ }
			{ "text" : '<meta name="author" content="Informatics", "Inc.">' }
			{ "regexp" : '/Web Application by <a href="http:\/\/www\.(ia-informatics|informaticsinc)\.com" [^>]*target="_blank"><b>Informatics", "Inc\.<\/b><\/a>/ }
		]

