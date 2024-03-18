import sys
import os
			
class Pluginantiboard_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "inurl", "ghdb" : "inurl:antiboard.php" },
			{ "name" : "powered by", "text" : "<a href=\"http://www.resynthesize.com/code/antiboard.php\">Powered by antiboard" },
		]
		return(self.rules)

