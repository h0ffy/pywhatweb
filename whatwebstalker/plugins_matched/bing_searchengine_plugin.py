import sys
import os
			
class Pluginbing_searchengine_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "var curUrl="http://www.bing.com/"" },
			{ "text" : "<meta content="Bing is a search engine that finds" },
		]

