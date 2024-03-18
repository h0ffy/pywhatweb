import sys
import os
			
class oracle_webdb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Oracle_WebDb_Listener\/([^\s]+)/ },
			{ "search" : 'headers[location]", "regexp" : '/^(https?:\/\/[^\/]+)?\/WebDB\/WEBDB\.home$/", "certainty" : '75 },
		]

