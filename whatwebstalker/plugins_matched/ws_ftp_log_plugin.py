import sys
import os
			
class ws_ftp_log_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/^[0-9]+.[0-9]{2}.[0-9]{2} [0-9]{2}:[0-9]{2} [A|B]{1} [^>]*> ([^\ ]+) / },
		]

