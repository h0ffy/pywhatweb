import sys
import os
			
class Pluginintrasrv_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^intrasrv ([\d\.]+)$/" },
		]
		return(self.rules)

