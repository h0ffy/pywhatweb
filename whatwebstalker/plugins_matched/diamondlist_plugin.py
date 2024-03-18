import sys
import os
			
class Plugindiamondlist_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.hulihanapplications.com/projects/diamondlist"><b>DiamondList</b>" },
		]
		return(self.rules)

