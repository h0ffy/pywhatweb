import sys
import os
			
class Pluginmongrel_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Mongrel ([\d][^\s]+)/" },
		]

