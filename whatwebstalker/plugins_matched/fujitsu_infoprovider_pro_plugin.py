import sys
import os
			
class Pluginfujitsu_infoprovider_pro_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/Fujitsu-InfoProvider-Pro/" },
			{ "search" : "headers[server]", "version" : "/Fujitsu-InfoProvider-Pro\/[V]?([^ ]+) /" },
		]
		return(self.rules)

