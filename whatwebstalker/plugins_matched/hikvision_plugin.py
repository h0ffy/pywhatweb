import sys
import os
			
class Pluginhikvision_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Hikvision-Webs$/" },
		]
		return(self.rules)

