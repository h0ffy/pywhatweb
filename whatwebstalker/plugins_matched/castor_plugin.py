import sys
import os
			
class castor_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/", "text" : '<html><head><title>CAStor Node Status</title></head><body><h2>CAStor Node IP' },
			{ "search" : 'headers[server]", "version" : '/^CAStor Cluster\/([^\s]+)$/ },
			{ "search" : 'headers[server]", "module" : /^CAStor (Reverse Proxy .+)$/ },
			{ "search" : 'headers[castor-system-totalgbavailable]", "regexp" : '/^[\d]+$/ },
			{ "search" : 'headers[castor-system-totalgbcapacity]", "regexp" : '/^[\d]+$/ },
		]

