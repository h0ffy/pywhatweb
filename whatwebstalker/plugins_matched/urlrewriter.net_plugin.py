import sys
import os
			
class Pluginurlrewriter.net_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-powered-by]", "version" : "/UrlRewriter\.NET ([^\s]+)/" },
		]
		return(self.rules)

