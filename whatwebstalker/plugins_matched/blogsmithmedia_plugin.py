import sys
import os
			
class Pluginblogsmithmedia_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "75", "regexp" : "/<script [^>]*\"http:\/\/www.blogsmithmedia.com},
		]

