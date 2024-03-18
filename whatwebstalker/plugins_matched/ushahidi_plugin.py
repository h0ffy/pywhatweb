import sys
import os
			
class Pluginushahidi_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "md5" : "7350c3f75cb80e857efa88c2fd136da5", "url" : "/favicon.ico" },
		]

