import sys
import os
			
class Pluginsentinelserver_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^SentinelServer/" },
		]
		return(self.rules)

