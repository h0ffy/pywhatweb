import sys
import os
			
class Pluginhighwire_press_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[x-firenze-processing-time]", "regexp" : "/^[\d\.]+$/" },
			{ "search" : "headers[x-firenze-processing-tims]", "regexp" : "/^detect-robot:/" },
			{ "search" : "headers[x-highwire-sessionid]", "regexp" : "/^.+$/" },
		]

