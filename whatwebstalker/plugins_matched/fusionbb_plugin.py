import sys
import os
			
class Pluginfusionbb_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/FusionBB&trade; Version (\d+\.?\d+?)/", "name" : "version" },
		]
		return(self.rules)

