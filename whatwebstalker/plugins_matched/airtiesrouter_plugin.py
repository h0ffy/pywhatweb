import sys
import os
			
class Pluginairtiesrouter_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<title>Airties ([^<]+)<},
		]

