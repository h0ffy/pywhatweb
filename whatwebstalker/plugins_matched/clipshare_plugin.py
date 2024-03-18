import sys
import os
			
class Pluginclipshare_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!--!!!!!!!!!!!!!!!!!!!!!!!!! Processing SCRIPT !!!!!!!!!!!!!!!!!!!-->" },
			{ "text" : "<!--!!!!!!!!!!!!!!!!!!!!!!!! LIBRARY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-->" },
			{ "text" : "Powered By <a href="http://www.clip-share.com">ClipShare</a>" },
		]

