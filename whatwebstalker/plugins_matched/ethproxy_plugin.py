import sys
import os
			
class Pluginethproxy_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^ethProxy$/" },
		]
		return(self.rules)

