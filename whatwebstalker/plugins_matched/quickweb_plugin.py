import sys
import os
			
class Pluginquickweb_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<HTML><HEAD><TITLE>QWScript Error</TITLE></HEAD>" },
		]
		return(self.rules)

