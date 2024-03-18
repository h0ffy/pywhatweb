import sys
import os
			
class Pluginbea_weblogic_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<title>Default BEA WebLogic Server Web Server Index Page</title>" },
			{ "text" : "<TITLE>Default BEA WebLogic Server Web Server Index Page</TITLE>" },
			{ "version" : "/<h1>BEA WebLogic Server ([^\s]+)&#153;<\/h1>/" },
			{ "search" : "headers[server]", "version" : "/^WebLogic( WebLogic)?( Server)? (.+)  [\d]{2}\/[\d]{2}\/[\d]{4}/", "offset" : "2 },
			{ "search" : "headers[server]", "version" : "/^WebLogic WebLogic (Temporary .+) [\d]{2}\/[\d]{2}\/[\d]{4}/" },
			{ "search" : "headers[server]", "version" : "/^WebLogic Server (.+) [A-Z][a-z]{2} [A-Z][a-z]{2} [\d]{1,2} [\d]{2}:[\d]{2}:[\d]{2}/" },
		]

