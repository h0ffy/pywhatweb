import sys
import os
			
class Pluginachecker_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<title>AChecker : ATRC Accessibility Checker: </title>" },
		]

