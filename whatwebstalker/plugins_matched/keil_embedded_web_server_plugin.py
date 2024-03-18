import sys
import os
			
class Pluginkeil_embedded_web_server_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<head><title>Keil Embedded WEB Server</title></head><body><h2>HTTP 1.0 401 Error. Unauthorized Access</h2>You are not authorized to access this server.<hr>" },
			{ "version" : "/^Keil-EWEB\/([^\s]+)$/", "search" : "headers[server]" },
			{ "regexp" : "/^Keil-EWEB/", "search" : "headers[server]" },
		]
		return(self.rules)

