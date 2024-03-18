import sys
import os
			
class Plugincontao_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "This website is powered by Contao Open Source CMS :: Licensed under GNU/LGPL'},
			{ "text" : "<!-- indexer::continue -->'},
		]

