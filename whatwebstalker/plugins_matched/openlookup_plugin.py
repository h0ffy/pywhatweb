import sys
import os
			
class Pluginopenlookup_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<h2>OpenLookup Node Status</h2>" },
			{ "version" : "/<p><a href="http:\/\/openlookup\.googlecode\.com\/">Source code and\n	further information<\/a> are available\.  This is OpenLookup V([^<]+)\.<\/p>/" },
		]

