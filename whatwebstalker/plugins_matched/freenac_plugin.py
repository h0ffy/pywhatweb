import sys
import os
			
class Pluginfreenac_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href="unknowns.php" title="List unknown end devices and print/edit/delete them">Find unknowns</a><br/>" },
		]
		return(self.rules)

