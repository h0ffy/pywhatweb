import sys
import os
			
class Pluginmicro_httpd_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/micro_httpd/i },
		]

