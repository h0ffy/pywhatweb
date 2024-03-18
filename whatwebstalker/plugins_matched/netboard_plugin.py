import sys
import os
			
class netboard_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : "inurl:"cgi-sys/netboard.cgi" filetype:cgi" },
			{ "text" : "<td><form method=post action="netboard.cgi">" },
			{ "text" : "<td><form method=post action=netboard.cgi>" },
		]

