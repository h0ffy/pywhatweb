import sys
import os
			
class Pluginlibwww_perl_daemon_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^libwww-perl-daemon\/([^\s]+)/" },
		]
		return(self.rules)

