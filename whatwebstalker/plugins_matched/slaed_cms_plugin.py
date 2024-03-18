import sys
import os
			
class Pluginslaed_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="SLAED CMS ([^"^>]+)">/" },
			{ "string" : /<br \/>Powered by <a href="http:\/\/www\.slaed\.net" target="_blank" title="SLAED CMS">SLAED CMS<\/a> &copy; 2005-(20[\d]{2}) SLAED/" },
		]

