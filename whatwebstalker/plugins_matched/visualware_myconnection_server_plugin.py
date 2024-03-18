import sys
import os
			
class Pluginvisualware_myconnection_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- Begin MyConnection Server applet -->" },
			{ "regexp" : "/^Visualware MyConnection Server/", "search" : "headers[server]" },
			{ "version" : "/^Visualware MyConnection Server [^\d]+ (\d\.[^\s]+)$/", "search" : "headers[server]" },
			{ "string" : /^Visualware MyConnection Server ([^\d]+) \d\.[^\s]+$/", "search" : "headers[server]" },
		]

