import sys
import os
			
class uportal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'powered by uportal"", "certainty" : '75 }
			{ "version" : '/<img[^>]*alt="Powered by uPortal ([\d\.]+)"[^>]*>/ }
			{ "version" : '/<a target="_blank" title="Powered by \$" href="http:\/\/www.uportal.org">Powered by uPortal ([^<]+)<\/a>/ }
	]

