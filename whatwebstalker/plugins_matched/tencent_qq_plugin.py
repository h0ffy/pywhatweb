import sys
import os
			
class Plugintencent_qq_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^HTTP_ME\/\d\.\d Tencent\/HTTP_Magic_Expression$/" },
		]
		return(self.rules)

