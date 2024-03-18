import sys
import os
			
class Pluginblue_coat_proxysg_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[location]", "regexp" : "/https?:\/\/proxysg\/\?cfru=[^\s]+$/" },
		]
		return(self.rules)

