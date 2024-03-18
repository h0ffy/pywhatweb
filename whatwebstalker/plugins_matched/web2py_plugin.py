import sys
import os
			
class Pluginweb2py_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-powered-by]", "string" : /web2py/" },
			{ "text" : "<div id="serendipityLeftSideBar">" },
		]
		return(self.rules)

