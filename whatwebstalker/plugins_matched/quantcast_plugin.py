import sys
import os
			
class Pluginquantcast_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "quant.js", "regexp" : "/<script[^>]+src=["']http:\/\/edge.quantserve.com\/quant.js["']/" },
		]
		return(self.rules)

