import sys
import os
			
class Pluginwildcat_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^[wW]ildcat\/v([^\s]+)/" },
			{ "search" : "headers[x-powered-by]", "version" : "/Wildcat.Net v([^\s]+)/" },
		]
		return(self.rules)

