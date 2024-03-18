import sys
import os
			
class libwww_perl_daemon_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^libwww-perl-daemon\/([^\s]+)/ }
		]

