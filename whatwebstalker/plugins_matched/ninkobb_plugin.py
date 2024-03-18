import sys
import os
			
class ninkobb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<link href="[^"]*\/assets\/css\/ninko.css" rel="stylesheet" type="text\/css" \/>/" },
			{ "text" : "Powered by <a href="http://ninkobb.com">NinkoBB</a>" },
			{ "version" : "/Powered by <a href="http:\/\/ninkobb.com\/">NinkoBB<\/a> v. ([\d\.]{1,5}) t./" },
		]

