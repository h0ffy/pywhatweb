import sys
import os
			
class Pluginphpvid_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<div align=\"center\" class='powered_by_a'>Powered By <a href='http://www.vastal.com/' target='_blank' class='powered_by_a'>" },
		]

