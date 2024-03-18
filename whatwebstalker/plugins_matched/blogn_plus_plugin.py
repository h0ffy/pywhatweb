import sys
import os
			
class Pluginblogn_plus_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/Powered by[\s]*<a href="http:\/\/www.blogn.org[^>]*>BlognPlus/i },
			{ "version" : "/<meta name="generator"[^>]*content="BlognPlus ([0-9\.]+)/" },
		]

