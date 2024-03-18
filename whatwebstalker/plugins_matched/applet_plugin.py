import sys
import os
			
class Pluginapplet_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "string" : /<applet[^>]+code[\s]*=[\s]*["|']?([^\s^>^"^']+)[^>]*>/i },
		]

