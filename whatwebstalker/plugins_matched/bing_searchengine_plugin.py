import sys
import os
			
class Pluginbing_searchengine_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "var curUrl="http://www.bing.com/"" },
			{ "text" : "<meta content="Bing is a search engine that finds" },
		]
		return(self.rules)

