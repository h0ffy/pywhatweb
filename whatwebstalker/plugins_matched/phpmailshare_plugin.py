import sys
import os
			
class phpmailshare_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div align="center">Powered by <a href="http:\/\/tekreaders\.com\/blog\/phpmailshare\/" target="_blank">phpMailShare<\/a> ([^<]+[\d\.\sa-z])<\/div>/ }
			{ "text" : '<a href="index.php?action=viewbox&amp;box=0">' }
	]

