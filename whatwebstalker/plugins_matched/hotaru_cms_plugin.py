import sys
import os
			
class Pluginhotaru_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="Hotaru CMS ([^\s^"^>]+)" \/>/" },
		]
		return(self.rules)

