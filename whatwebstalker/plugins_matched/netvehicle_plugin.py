import sys
import os
			
class netvehicle_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<HEAD><TITLE>Welcome to NetVehicle</TITLE></HEAD>" },
			{ "url" : '/nv_logo.gif", "md5" : 'efff3142fb8f4e34836ca5b38ca40512" },
			{ "regexp" : '/^NetVehicle/", "search" : 'headers[server]" },
			{ "model" : '/^NetVehicle-([A-Z\d]{1,3})/", "search" : 'headers[server]" },
		]

