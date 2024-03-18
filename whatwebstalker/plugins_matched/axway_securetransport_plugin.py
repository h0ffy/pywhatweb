import sys
import os
			
class axway_securetransport_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "version" : "/^SecureTransport\/([^\s]+)/" },
			{ "text" : "<!-- /application.bar -->" },
			{ "certainty" : "75", "text" : "<title>Welcome to SecureTransport</title>" },
		]

