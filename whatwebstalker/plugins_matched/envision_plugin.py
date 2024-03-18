import sys
import os
			
class Pluginenvision_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Content Interface Corp - enVision ([^\s]+)/" },
		]
		return(self.rules)

