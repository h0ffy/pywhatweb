import sys
import os
			
class Pluginpommo_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Page fueled by <a href="http://www.pommo.org/">poMMo</a> mailing management software" },
			{ "text" : "Page fueled by <a href="http://pommo.sourceforge.net/">poMMo</a> mailing management software" },
			{ "text" : "<title>. ..poMMo.. .</title>" },
		]

