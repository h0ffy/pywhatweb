import sys
import os
			
class Plugingordano_messaging_suite_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Gordano (Messaging Suite )?Web Server v([^\s]+)$/", "offset" : "1 },
		]

