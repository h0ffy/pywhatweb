import sys
import os
			
class Pluginintrinsyc_deviceweb_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Intrinsyc deviceWEB v([\d\.]+)$/" },
		]
		return(self.rules)

