import sys
import os
			
class Pluginsyntype_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="synType CMS" />" },
			{ "text" : "width="150" height="40" border="0" alt="This Web site is powered by synType CMS", "the ultimate Content Management System" /></a>" },
		]
		return(self.rules)

