import sys
import os
			
class Pluginblue_coat_proxysg_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[location]", "regexp" : "/https?:\/\/proxysg\/\?cfru=[^\s]+$/" },
		]

