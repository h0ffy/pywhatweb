import sys
import os
			
class Pluginwolfcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/png" \/> Wolf CMS ([^<]+)<\/div>},
			{ "regexp" : "/href="http:\/\/www.wolfcms.org\/" title="Wolf CMS" rel="noreferrer">Wolf CMS<\/a>[\s]+Inside.},
		]

