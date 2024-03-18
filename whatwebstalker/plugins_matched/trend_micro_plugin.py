import sys
import os
			
class trend_micro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Trend Micro$/ },
			{ "search" : 'headers[server]", "version" : '/^Trend Micro ([^\s]+)$/ },
		]

