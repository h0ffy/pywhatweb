import sys
import os
			
class Pluginblogsmithmedia_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "regexp" : "/<script [^>]*\"http:\/\/www.blogsmithmedia.com},
		]
		return(self.rules)

