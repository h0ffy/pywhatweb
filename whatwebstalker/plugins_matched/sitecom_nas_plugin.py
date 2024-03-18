import sys
import os
			
class sitecom_nas_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "search" : 'headers[www-authenticate]", "text" : 'Basic realm="SITECOM LOGIN Enter Password (default is sitecom)' }
		]

