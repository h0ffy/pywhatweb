import sys
import os
			
class urlrewriter.net_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-powered-by]", "version" : '/UrlRewriter\.NET ([^\s]+)/ }
		]

