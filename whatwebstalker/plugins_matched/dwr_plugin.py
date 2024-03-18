import sys
import os
			
class Plugindwr_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "HTML Body',"text" : "/dwr/engine.js\'>'},
			{ "name" : "HTML Body',"text" : "/dwr/engine.js">'},
		]
		return(self.rules)

