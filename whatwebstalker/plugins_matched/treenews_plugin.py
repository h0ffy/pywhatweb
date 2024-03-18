import sys
import os
			
class treenews_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/vendor.js", "string" : /var _VENDOR_ = "([^"]+)";/ }
			{ "url" : '/vendor.js", "model" : '/var _OTHER_SYSTEM_MANAGEMENT_NAME_ = '([^']+)';/ }
			{ "search" : 'headers[server]", "version" : '/^TreeNeWS\/([^\s]+)$/ }
		]

