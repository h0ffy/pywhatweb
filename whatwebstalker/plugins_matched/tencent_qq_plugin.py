import sys
import os
			
class Plugintencent_qq_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^HTTP_ME\/\d\.\d Tencent\/HTTP_Magic_Expression$/" },
		]

