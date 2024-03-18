import sys
import os
			
class Pluginhp_printer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "model" : "/^HP HTTP Server; HP (.+) series - /" },
		]

