import sys
import os
			
class Pluginpommo_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Page fueled by <a href="http://www.pommo.org/">poMMo</a> mailing management software" },
			{ "text" : "Page fueled by <a href="http://pommo.sourceforge.net/">poMMo</a> mailing management software" },
			{ "text" : "<title>. ..poMMo.. .</title>" },
		]
		return(self.rules)

