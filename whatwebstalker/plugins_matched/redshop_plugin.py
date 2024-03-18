import sys
import os
			
class redshop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by:<a href="http://www.rednetcms.com/redshop" target="_blank">Redshop</a>' }
			{ "text" : '<link href="images/redcms.css" rel="stylesheet" type="text/css" />' }
		]

