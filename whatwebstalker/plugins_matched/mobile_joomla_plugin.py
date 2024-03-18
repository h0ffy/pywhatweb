import sys
import os
			
class Pluginmobile_joomla_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/mjmarkup=deleted;/" },
		]
		return(self.rules)

