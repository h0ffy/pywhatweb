import sys
import os
			
class Pluginextjs_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["'][^>]*ext\-base\.js["']/i },
		]
		return(self.rules)

