import sys
import os
			
class keil_embedded_web_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<head><title>Keil Embedded WEB Server</title></head><body><h2>HTTP 1.0 401 Error. Unauthorized Access</h2>You are not authorized to access this server.<hr>' },
			{ "version" : '/^Keil-EWEB\/([^\s]+)$/", "search" : 'headers[server]" },
			{ "regexp" : '/^Keil-EWEB/", "search" : 'headers[server]" },
		]

