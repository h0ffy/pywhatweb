import sys
import os
			
class Pluginaladdin_hasp_license_manager_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^HASP LM\/([^\s]+)$/" },
		]
		return(self.rules)

