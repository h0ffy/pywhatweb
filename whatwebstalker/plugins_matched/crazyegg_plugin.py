import sys
import os
			
class Plugincrazyegg_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "cetrk.com" },
			{ "account" : "/dnn506yrbagrg\.cloudfront\.net\/pages\/scripts\/(\d+\/\d+)},
		]

