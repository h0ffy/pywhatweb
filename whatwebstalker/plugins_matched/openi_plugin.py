import sys
import os
			
class Pluginopeni_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<span class="big-title">Openi ([^\s^<]+)<\/span><br/" },
			{ "string" : /<span class="big-title">Openi-(Jasper)<\/span><br/" },
		]
		return(self.rules)

