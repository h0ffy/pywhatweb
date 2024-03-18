import sys
import os
			
class Pluginnetcache_appliance_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^NetCache appliance \(NetApp\/([^\)]+)\)$/" },
		]
		return(self.rules)

