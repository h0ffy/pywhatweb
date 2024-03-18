import sys
import os
			
class Pluginw3mfc_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^W3MFC\/([\d\.]+)$/  },
		]
		return(self.rules)

