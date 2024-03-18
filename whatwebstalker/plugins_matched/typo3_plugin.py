import sys
import os
			
class typo3_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="generator" content="TYPO3 ([\d\.]+) CMS"/ }
			{ "text" : '<!--TYPO3SEARCH_end-->", "certainty" : '75 }
			{ "name" : 'Powered by HTML comment", "regexp" : '/<!--\W+This website is powered by TYPO3/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/^fe_typo_user/", "name" : 'fe_typo_user cookie" }
			{ "search" : 'headers[x-typo3-parsetime]", "regexp" : '/\d+ms/", "name" : 'X-TYPO3-Parsetime header" }
		]

