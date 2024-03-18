import sys
import os
			
class bigdump_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<h1>BigDump: Staggered MySQL Dump Importer ver\. ([^\s^<]{2,6})<\/h1>/ }
			{ "version" : '/<title>BigDump ver\. ([^\s^<]{2,6})<\/title>/ }
		]

