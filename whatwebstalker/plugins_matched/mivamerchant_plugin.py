import sys
import os
			
class Pluginmivamerchant_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<div id="mmcategorytree">" },
			{ "ghdb" : "inurl:merchant.mvc filetype:mvc" },
			{ "search" : "headers[set-cookie]", "regexp" : "/htscallerid=/" },
		]

