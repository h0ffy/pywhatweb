import sys
import os
			
class Plugindavid_webbox_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^David-WebBox\/([^\s]+ \([^\)]+\))$/" },
		]

