import sys
import os
			
class Pluginwebsitepro_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^WebSitePro\/([^\s]+)/" },
		]
		return(self.rules)

