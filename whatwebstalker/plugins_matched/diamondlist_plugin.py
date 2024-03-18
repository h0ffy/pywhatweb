import sys
import os
			
class Plugindiamondlist_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.hulihanapplications.com/projects/diamondlist"><b>DiamondList</b>" },
		]

