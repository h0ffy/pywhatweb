import sys
import os
			
class Plugindeluge_web_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>Deluge: Web UI ([^<]+)<\/title>},
		]
		return(self.rules)

