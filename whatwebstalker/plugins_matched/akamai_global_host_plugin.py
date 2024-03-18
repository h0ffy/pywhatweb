import sys
import os
			
class Pluginakamai_global_host_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^AkamaiGHost/" },
		]
		return(self.rules)

