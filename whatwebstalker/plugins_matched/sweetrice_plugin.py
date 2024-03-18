import sys
import os
			
class sweetrice_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="generator" content="SweetRice ([\d\.]{1,5})" \/>/ }
			{ "text" : 'Powered By <a href="http://www.basic-cms.org">Basic CMS SweetRice</a>' }
		]

