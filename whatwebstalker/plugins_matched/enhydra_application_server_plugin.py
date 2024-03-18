import sys
import os
			
class Pluginenhydra_application_server_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Enhydra-MultiServer\/([^\s]+)/" },
			{ "search" : "headers[servlet-engine]", "version" : "/Enhydra Application Server\/([^\s]+)/" },
		]
		return(self.rules)

