import sys
import os
			
class Pluginintrinsyc_deviceweb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Intrinsyc deviceWEB v([\d\.]+)$/" },
		]

