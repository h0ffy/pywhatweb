import sys
import os
			
class fcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="author" content="Ryan Haudenschilt"/>' }
			{ "regexp" : '/- [pP]owered by Family Connections<\/title>/ }
			{ "version" : '/- [pP]owered by Family Connections ([^\s^<]+)[\s]*<\/title>[\s]*(<meta|<link)/ }
		]

