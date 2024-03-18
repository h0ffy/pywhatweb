import sys
import os
			
class keyfocus_webserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^KFWebServer$/ }
			{ "search" : 'headers[server]", "version" : '/^KFWebServer\/([\d\.]+)/ }
		]

