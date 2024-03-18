import sys
import os
			
class Pluginwikidforum_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.wikidforum.com" title="wikidforum.com">WikidForum</a>" },
		]

