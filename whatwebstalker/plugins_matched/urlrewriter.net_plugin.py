import sys
import os
			
class Pluginurlrewriter.net_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[x-powered-by]", "version" : "/UrlRewriter\.NET ([^\s]+)/" },
		]

