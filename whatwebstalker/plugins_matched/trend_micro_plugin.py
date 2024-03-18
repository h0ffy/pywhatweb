import sys
import os
			
class Plugintrend_micro_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Trend Micro$/" },
			{ "search" : "headers[server]", "version" : "/^Trend Micro ([^\s]+)$/" },
		]
		return(self.rules)

