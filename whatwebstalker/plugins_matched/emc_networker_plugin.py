import sys
import os
			
class Pluginemc_networker_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Welcome to NetWorker Management Console</title>" },
		]
		return(self.rules)

