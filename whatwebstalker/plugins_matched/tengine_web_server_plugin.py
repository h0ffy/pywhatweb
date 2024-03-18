import sys
import os
			
class Plugintengine_web_server_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Tengine$/" },
			{ "search" : "headers[server]", "version" : "/^Tengine\/([^\s]+)/" },
		]
		return(self.rules)

