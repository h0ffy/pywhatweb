import sys
import os
			
class Pluginhotaru_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="Hotaru CMS ([^\s^"^>]+)" \/>/" },
		]

