import sys
import os
			
class lotus_domino_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "ghdb" : 'filetype:nsf' }
			{ "search" : 'headers[server]", "version" : '/^Lotus-Domino\/([^\s]+)/ }
			{ "search" : 'headers[server]", "regexp" : '/^Lotus-Domino$/ }
			{ "certainty" : '75", "url" : '/favicon.ico", "md5" : '639b61409215d770a99667b446c80ea1" }
		]

