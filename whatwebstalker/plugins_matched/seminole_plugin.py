import sys
import os
			
class Pluginseminole_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Seminole\/([^\s]+)/" },
		]
		return(self.rules)

