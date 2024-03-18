import sys
import os
			
class Pluginfastpublish_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "url" : "favicon.ico", "md5" : "e95aa1d29e576c9ebdb08e0c5160cdfa" },
			{ "version" : "/<meta name="Generator" content="fastpublish CMS ([^"]{1,15})">/" },
		]

