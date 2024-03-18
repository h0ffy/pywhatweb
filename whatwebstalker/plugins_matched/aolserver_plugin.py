import sys
import os
			
class Pluginaolserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^AOLserver$/" },
			{ "search" : "headers[server]", "version" : "/^AOLserver\/([^\s]+)/" },
		]

