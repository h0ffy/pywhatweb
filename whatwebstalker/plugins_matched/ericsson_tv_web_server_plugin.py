import sys
import os
			
class Pluginericsson_tv_web_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server ]", "regexp" : "/^Ericsson Television Web server$/" },
		]

