import sys
import os
			
class Pluginplay_framework_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Play! Framework;(\d[^\s^;]+;[^\s]+)$/" },
		]
		return(self.rules)

