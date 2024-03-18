import sys
import os
			
class thehostingtool_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div id="footer">Powered by <a href="http:\/\/thehostingtool.com" target="_blank">TheHostingTool<\/a> ([\d\.]*)<\/div>/ }
	]

