import sys
import os
			
class Pluginenhydra_application_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Enhydra-MultiServer\/([^\s]+)/" },
			{ "search" : "headers[servlet-engine]", "version" : "/Enhydra Application Server\/([^\s]+)/" },
		]

