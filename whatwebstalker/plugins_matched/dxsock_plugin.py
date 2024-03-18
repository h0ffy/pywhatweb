import sys
import os
			
class dxsock_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^RemObjects DXSock Web Server/ }
			{ "search" : 'headers[user-agent]", "regexp" : '/^RemObjects SDK$/ }
	]

