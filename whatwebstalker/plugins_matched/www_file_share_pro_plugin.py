import sys
import os
			
class Pluginwww_file_share_pro_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td height="27"><a href="http://www.lionmax.com" target="_blank">Powered by LionMax Software</a></td>" },
		]
		return(self.rules)

