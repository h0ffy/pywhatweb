import sys
import os
			
class Pluginoracle_internet_application_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Oracle9iAS\/([^\s]+)/" },
			{ "search" : "headers[server]", "version" : "/^Oracle9iAS \(([^\s^\)]+)\)/" },
			{ "search" : "headers[server]", "module" : /^Oracle9iAS.+ (Oracle9iAS-Web-Cache\/[^\s]+)/" },
		]

