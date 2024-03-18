import sys
import os
			
class koala_web_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "regexp" : "/^Koala Web Server/" },
			{ "search" : "headers[server]", "version" : "/^Koala Web Server\/([^\s]+)/" },
		]

