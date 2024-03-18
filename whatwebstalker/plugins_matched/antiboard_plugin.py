import sys
import os
			
class Pluginantiboard_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "name" : "inurl", "ghdb" : "inurl:antiboard.php" },
			{ "name" : "powered by", "text" : "<a href=\"http://www.resynthesize.com/code/antiboard.php\">Powered by antiboard" },
		]

