import sys
import os
			
class statusnet_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<p>This site is powered by <a href="http:\/\/status\.net\/">StatusNet<\/a> version ([^\s]+),/ }
			{ "version" : '/It runs the <a href="http:\/\/status\.net\/">StatusNet<\/a> microblogging software", "version ([^\s]+)", "available under the <a / }
	]

