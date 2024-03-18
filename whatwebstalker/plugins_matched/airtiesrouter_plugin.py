import sys
import os
			
class Pluginairtiesrouter_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>Airties ([^<]+)<},
		]
		return(self.rules)

