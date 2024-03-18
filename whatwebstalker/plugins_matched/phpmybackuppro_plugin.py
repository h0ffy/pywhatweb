import sys
import os
			
class phpmybackuppro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[www-authenticate]", "regexp" : '/[bB]asic realm="phpMyBackupPro"/ },
			{ "text" : 'Please login (use your MySQL username and password): <a href="index.php?login=TRUE">Login</a>' },
		]

