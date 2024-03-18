import sys
import os
			
class Pluginphpmytourney_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href=\"http://phpmytourney.sourceforge.net/\"><font face='Arial' size='1'>phpMyTourney</font> </a>" },
			{ "text" : "ERROR : page not properly called" },
		]

