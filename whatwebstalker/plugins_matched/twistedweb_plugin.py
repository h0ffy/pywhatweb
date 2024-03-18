import sys
import os
			
class Plugintwistedweb_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/TwistedWeb\/?([^ ]+)?/", "search" : "headers[server]"},
		]
		return(self.rules)

