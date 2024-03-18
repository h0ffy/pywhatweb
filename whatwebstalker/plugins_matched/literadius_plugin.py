import sys
import os
			
class Pluginliteradius_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "inurl:locator.php parsed_page lat long" },
		]
		return(self.rules)

