import sys
import os
			
class Pluginfizmez_web_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Fizmez\/0\.0\.1/", "version" : "1.0" },
			{ "search" : "headers[server]", "version" : "/^Fizmez\/([1-9]+\.[\d\.]+)/" },
		]

