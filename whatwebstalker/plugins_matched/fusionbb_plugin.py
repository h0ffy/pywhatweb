import sys
import os
			
class Pluginfusionbb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/FusionBB&trade; Version (\d+\.?\d+?)/", "name" : "version" },
		]

