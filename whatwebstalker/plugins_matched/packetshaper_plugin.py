import sys
import os
			
class Pluginpacketshaper_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>PacketShaper Customer Login</title>" },
			{ "text" : "<SCRIPT LANGUAGE=JavaScript SRC="/libmd5.js"></SCRIPT>" },
		]
		return(self.rules)

