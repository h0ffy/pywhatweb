import sys
import os
			
class dell_printer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "model" : '/<title>Dell Laser Printer ([A-Z]?[\d]{4}[a-z]{0,2})<\/title>/i }
			{ "model" : '/<TITLE>Dell ([\d]{4}[a-z]+) Laser Printer<\/TITLE>/ }
	]

