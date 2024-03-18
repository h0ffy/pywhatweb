import sys
import os
			
class Pluginnetapp_nas_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^NetApp\/(.+)$/" },
		]
		return(self.rules)

