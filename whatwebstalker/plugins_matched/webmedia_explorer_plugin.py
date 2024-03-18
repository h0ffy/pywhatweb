import sys
import os
			
class webmedia_explorer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/Powered by <a href="http:\/\/www.webmediaexplorer.com[^>]*>webmedia explorer ([\d\.]+)<\/a>/i }
	]

