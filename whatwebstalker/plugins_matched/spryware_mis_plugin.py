import sys
import os
			
class Pluginspryware_mis_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^SpryWare\/([^\s]+)$/" },
			{ "search" : "headers[x-deprecated-response]", "regexp" : "/^Invalid CheckSum Received$/" },
		]
		return(self.rules)

