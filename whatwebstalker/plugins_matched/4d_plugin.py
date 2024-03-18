import sys
import os
			
class Plugin4d_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^4D_v[\d]{1,2}(_SQL)?\/([\d\.]+)$/", "offset" : "1 },
		]
		return(self.rules)

