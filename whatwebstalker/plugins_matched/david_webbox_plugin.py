import sys
import os
			
class Plugindavid_webbox_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^David-WebBox\/([^\s]+ \([^\)]+\))$/" },
		]
		return(self.rules)

