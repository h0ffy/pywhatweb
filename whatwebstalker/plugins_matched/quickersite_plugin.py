import sys
import os
			
class quickersite_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<meta content="QuickerSite CMS - visit www.quickersite.com" name="generator" \/>/i }
			{ "regexp" : '/<meta name="generator" content="QuickerSite CMS - visit www.quickersite.com">/i }
	]

