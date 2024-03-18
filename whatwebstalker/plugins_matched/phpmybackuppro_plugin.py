import sys
import os
			
class Pluginphpmybackuppro_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[www-authenticate]", "regexp" : "/[bB]asic realm="phpMyBackupPro"/" },
			{ "text" : "Please login (use your MySQL username and password): <a href="index.php?login=TRUE">Login</a>" },
		]
		return(self.rules)

