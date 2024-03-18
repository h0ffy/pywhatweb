import sys
import os
			
class Plugintoshiba_printer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<TITLE CLASS="clsTitle1">TopAccess</title>" },
		]

