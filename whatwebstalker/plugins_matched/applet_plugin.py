import sys
import os
			
class Pluginapplet_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<applet[^>]+code[\s]*=[\s]*["|']?([^\s^>^"^']+)[^>]*>/i },
		]
		return(self.rules)

