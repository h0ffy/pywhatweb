import sys
import os
			
class Pluginweb2py_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[x-powered-by]", "string" : /web2py/" },
			{ "text" : "<div id="serendipityLeftSideBar">" },
		]

