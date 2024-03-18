import sys
import os
			
class Pluginliteradius_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "ghdb" : "inurl:locator.php parsed_page lat long" },
		]

