import sys
import os
			
class Pluginwatson_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<TITLE>Watson Management Console</TITLE>" },
			{ "text" : "<!--- Page(page_login)=[Login] ---><HTML>"},
		]

