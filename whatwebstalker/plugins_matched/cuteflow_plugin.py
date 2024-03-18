import sys
import os
			
class cuteflow_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<a href="http:\/\/cuteflow\.org" target="_blank"><img src="images\/cuteflow_logo_small\.png" border="0"\s?\/><\/a><br>\s+<strong style="font-size:8pt;font-weight:normal">Version ([^\s^<]+)<\/strong><br>/ },
			{ "search" : 'headers[set-cookie]", "regexp" : '/^strMyLanguage=/ },
		]

