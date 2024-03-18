import sys
import os
			
class fujitsu_infoprovider_pro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "regexp" : "/Fujitsu-InfoProvider-Pro/" },
			{ "search" : "headers[server]", "version" : "/Fujitsu-InfoProvider-Pro\/[V]?([^ ]+) /" },
		]

