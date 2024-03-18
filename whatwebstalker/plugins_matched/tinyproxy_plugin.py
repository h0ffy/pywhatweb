import sys
import os
			
class Plugintinyproxy_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^tinyproxy\/([^\s]+)/" },
		]
		return(self.rules)

