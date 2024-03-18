import sys
import os
			
class Plugindeluge_web_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<title>Deluge: Web UI ([^<]+)<\/title>},
		]

