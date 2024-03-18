import sys
import os
			
class net2ftp_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "text" : '<title>net2ftp - a web based FTP client</title>' }
			{ "version" : '/<!-- net2ftp version ([^\s]+) -->/ }
			{ "text" : '<!-- End of net2ftp login form -->' }
	]

