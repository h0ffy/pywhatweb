import sys
import os
			
class Pluginkoala_web_server_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Koala Web Server/" },
			{ "search" : "headers[server]", "version" : "/^Koala Web Server\/([^\s]+)/" },
		]
		return(self.rules)

