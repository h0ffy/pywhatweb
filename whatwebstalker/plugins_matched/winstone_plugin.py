import sys
import os
			
class Pluginwinstone_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Winstone Servlet Engine v([^\s]+)/" },
			{ "search" : "headers[x-powered-by]", "version" : "/Servlet\/[^\s]+ \(Winstone\/([^\)]+)\)/" },
		]
		return(self.rules)

