import sys
import os
			
class Pluginxavante_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Xavante (.+)$/" },
		]
		return(self.rules)

