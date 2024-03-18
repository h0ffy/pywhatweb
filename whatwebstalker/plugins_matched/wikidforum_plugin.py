import sys
import os
			
class Pluginwikidforum_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.wikidforum.com" title="wikidforum.com">WikidForum</a>" },
		]
		return(self.rules)

