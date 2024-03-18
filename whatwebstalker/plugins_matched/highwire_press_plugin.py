import sys
import os
			
class Pluginhighwire_press_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-firenze-processing-time]", "regexp" : "/^[\d\.]+$/" },
			{ "search" : "headers[x-firenze-processing-tims]", "regexp" : "/^detect-robot:/" },
			{ "search" : "headers[x-highwire-sessionid]", "regexp" : "/^.+$/" },
		]
		return(self.rules)

