import sys
import os
			
class Pluginphpmailshare_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div align="center">Powered by <a href="http:\/\/tekreaders\.com\/blog\/phpmailshare\/" target="_blank">phpMailShare<\/a> ([^<]+[\d\.\sa-z])<\/div>/" },
			{ "text" : "<a href="index.php?action=viewbox&amp;box=0">" },
		]
		return(self.rules)

