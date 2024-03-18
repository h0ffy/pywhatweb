import sys
import os
			
class Pluginmivamerchant_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="mmcategorytree">" },
			{ "ghdb" : "inurl:merchant.mvc filetype:mvc" },
			{ "search" : "headers[set-cookie]", "regexp" : "/htscallerid=/" },
		]
		return(self.rules)

