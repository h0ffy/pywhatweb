import sys
import os
			
class Pluginw3mfc_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^W3MFC\/([\d\.]+)$/  },
		]

