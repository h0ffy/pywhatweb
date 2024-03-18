import sys
import os
			
class Pluginmyzone_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>MyZone<\/title>.*www\.netcomm\.com\.au/m},
		]
		return(self.rules)

