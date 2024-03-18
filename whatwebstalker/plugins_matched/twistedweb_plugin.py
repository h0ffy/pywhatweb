import sys
import os
			
class Plugintwistedweb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/TwistedWeb\/?([^ ]+)?/", "search" : "headers[server]"},
		]

