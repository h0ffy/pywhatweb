import sys
import os
			
class applet_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<applet[^>]+code[\s]*=[\s]*["|']?([^\s^>^"^']+)[^>]*>/i }
	]

