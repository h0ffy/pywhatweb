import sys
import os
			
class isolsoft_support_center_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<strong><font color="#FF0000">Warning! This heldesk requires a browser with javascript ' }
			{ "text" : '<!-- Copyright Line: Unauthorized removal can void license -->' }
			{ "version" : '/<p align="center"><font size="1">Powered by: Support Center v([^<^\s]+)<br>/ }
		]

