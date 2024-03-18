import sys
import os
			
class Pluginaxis_printserver_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<h2>Welcome to AXIS 540/542 Network Print Server</h2>'},
			{ "url" : "/", "model" : "/<h2>Welcome to AXIS.*<hr><p>Name: ([\S]+)<br>/m},
			{ "url" : "/", "version" : "/<h2>Welcome to AXIS.*Software version: ([0-9\.]+)<br>/m},
		]
		return(self.rules)

