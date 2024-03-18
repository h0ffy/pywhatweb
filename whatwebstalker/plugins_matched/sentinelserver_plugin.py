import sys
import os
			
class sentinelserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^SentinelServer/ },
		]

