import sys
import os
			
class alpha_five_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Alpha Five( Application Server)?\/([\d\.]+ Build\/[\d\-]+)/", "offset" : '1 }
			{ "search" : 'headers[set-cookie]", "regexp" : '/A5wSessionId=[a-f\d]{32};/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/A5wBrowserId=[a-f\d]{32};/ }
		]

