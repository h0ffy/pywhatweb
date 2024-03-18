import sys
import os
			
class Pluginsiemens_router_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[www-authenticate]", "model" : "/Basic realm="Siemens ADSL ([^"^\s]+)"/", "certainty" : "75 },
		]
		return(self.rules)

