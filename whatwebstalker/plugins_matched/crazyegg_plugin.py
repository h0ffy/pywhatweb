import sys
import os
			
class Plugincrazyegg_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "cetrk.com" },
			{ "account" : "/dnn506yrbagrg\.cloudfront\.net\/pages\/scripts\/(\d+\/\d+)},
		]
		return(self.rules)

