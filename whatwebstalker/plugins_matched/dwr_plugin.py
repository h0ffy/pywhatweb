import sys
import os
			
class Plugindwr_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "name" : "HTML Body',"text" : "/dwr/engine.js\'>'},
			{ "name" : "HTML Body',"text" : "/dwr/engine.js">'},
		]

