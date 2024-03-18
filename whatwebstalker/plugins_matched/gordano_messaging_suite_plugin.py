import sys
import os
			
class Plugingordano_messaging_suite_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Gordano (Messaging Suite )?Web Server v([^\s]+)$/", "offset" : "1 },
		]
		return(self.rules)

