import sys
import os
			
class Pluginnet2phone_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<HTML><HEAD><TITLE>Net2Phone Init Page</TITLE>" },
			{ "model" : "/<P align=center><IMG border=0[\s]+src="([a-zA-Z]{2}[\d]+[a-zA-Z]?)\.gif" width="/" },
		]

