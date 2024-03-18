import sys
import os
			
class Plugintypolight_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "name" : "typolight.css", "text" : "<link rel="stylesheet" href="system/typolight.css" type="text/css" media="screen" />'},
			{ "text" : "This website is powered by TYPOlight Open Source CMS :: Licensed under GNU/LGPL'},
			{ "text" : "<!-- indexer::continue -->'},
		]

