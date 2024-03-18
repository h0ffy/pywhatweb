import sys
import os
			
class oracle_database_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Oracle XML DB\/Oracle Database$/", "module" : 'Oracle XML DB" }
		]

