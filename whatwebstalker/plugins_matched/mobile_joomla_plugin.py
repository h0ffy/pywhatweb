import sys
import os
			
class Pluginmobile_joomla_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/mjmarkup=deleted;/" },
		]

