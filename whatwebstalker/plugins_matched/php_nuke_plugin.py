import sys
import os
			
class Pluginphp_nuke_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "75", "module" : /<a href="[^"]*modules.php\?name=([a-zA-Z0-9_]+)[^"]*">/" },
		]

