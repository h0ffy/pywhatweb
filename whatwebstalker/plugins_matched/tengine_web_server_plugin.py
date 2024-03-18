import sys
import os
			
class Plugintengine_web_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Tengine$/" },
			{ "search" : "headers[server]", "version" : "/^Tengine\/([^\s]+)/" },
		]

