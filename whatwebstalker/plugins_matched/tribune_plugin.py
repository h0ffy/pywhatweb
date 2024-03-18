import sys
import os
			
class Plugintribune_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" :  '<a href="http://www.tribune.com/" target="_parent">A Tribune Newspaper website</a>" },
		]

