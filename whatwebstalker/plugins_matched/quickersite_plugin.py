import sys
import os
			
class Pluginquickersite_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta content="QuickerSite CMS - visit www.quickersite.com" name="generator" \/>/i },
			{ "regexp" : "/<meta name="generator" content="QuickerSite CMS - visit www.quickersite.com">/i },
		]
		return(self.rules)

