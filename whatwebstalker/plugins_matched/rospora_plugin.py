import sys
import os
			
class Pluginrospora_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<link rel="Shortcut Icon" href="img/wowlogoanim.gif" type="image/gif">" },
			{ "text" : "<li>This server supports only 2.2.3 clients<br><li>1x Quest XP ", "1x Kill XP ", "1x Discovery XP" },
		]

