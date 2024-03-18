import sys
import os
			
class Pluginspecialix_jetstream_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Specialix JETSTREAM ([\d\.]+)$/" },
		]
		return(self.rules)

