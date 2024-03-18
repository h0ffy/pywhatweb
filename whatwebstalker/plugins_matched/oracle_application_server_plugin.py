import sys
import os
			
class oracle_application_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "string" : /^Oracle-Application-Server-(1[01]g)/ }
			{ "search" : 'headers[server]", "version" : '/^Oracle-Application-Server-1[01]g\/([^\s]+)/ }
			{ "search" : 'headers[server]", "version" : '/^Oracle Application Server\/1[01]g \(([^\s^\)]+)\)/ }
			{ "search" : 'headers[server]", "module" : /^Oracle[ -]Application[ -]Server.+ (OracleAS-Web-Cache-1[01]g\/[^\s]+)/ }
	]

