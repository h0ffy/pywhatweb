import sys
import os
			
class 4d_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^4D_v[\d]{1,2}(_SQL)?\/([\d\.]+)$/", "offset" : '1 }
	]

