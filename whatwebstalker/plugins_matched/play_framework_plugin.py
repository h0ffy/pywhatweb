import sys
import os
			
class Pluginplay_framework_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Play! Framework;(\d[^\s^;]+;[^\s]+)$/" },
		]

