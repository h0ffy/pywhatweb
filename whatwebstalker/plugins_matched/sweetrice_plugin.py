import sys
import os
			
class Pluginsweetrice_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="SweetRice ([\d\.]{1,5})" \/>/" },
			{ "text" : "Powered By <a href="http://www.basic-cms.org">Basic CMS SweetRice</a>" },
		]
		return(self.rules)

