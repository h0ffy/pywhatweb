import sys
import os
			
class aladdin_hasp_license_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "version" : "/^HASP LM\/([^\s]+)$/" },
		]

