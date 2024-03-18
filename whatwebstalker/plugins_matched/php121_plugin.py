import sys
import os
			
class php121_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>PHP121 - Please login or register</title>' }
			{ "text" : '<title>PHP121 - New User</title>' }
			{ "version" : '/<center>Powered by <a target="_blank" style="TEXT-DECORATION: none; COLOR: #000066; FONT-SIZE: 10px" href="http:\/\/www.php121.com"><U>PHP121<\/U><\/a> v([\d\.]+)<\/center>/ }
	]

