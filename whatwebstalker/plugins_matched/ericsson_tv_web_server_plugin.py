import sys
import os
			
class Pluginericsson_tv_web_server_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server ]", "regexp" : "/^Ericsson Television Web server$/" },
		]
		return(self.rules)

