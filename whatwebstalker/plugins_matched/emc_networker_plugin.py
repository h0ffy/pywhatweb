import sys
import os
			
class Pluginemc_networker_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<title>Welcome to NetWorker Management Console</title>" },
		]

