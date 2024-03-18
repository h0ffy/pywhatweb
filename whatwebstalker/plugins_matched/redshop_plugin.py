import sys
import os
			
class Pluginredshop_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by:<a href="http://www.rednetcms.com/redshop" target="_blank">Redshop</a>" },
			{ "text" : "<link href="images/redcms.css" rel="stylesheet" type="text/css" />" },
		]
		return(self.rules)

