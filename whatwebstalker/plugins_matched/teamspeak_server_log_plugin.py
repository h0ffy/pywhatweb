import sys
import os
			
class teamspeak_server_log_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/^[0-9]{2}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},ALL,Info,server,[\s]+Server version: ([^\r^\n]+)/ }
		]

