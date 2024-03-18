import sys
import os
			
class Pluginmark_of_the_web_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<!-- saved from url=\([\d]+\)([^>]+) -->[\r\n]/" },
		]
		return(self.rules)

