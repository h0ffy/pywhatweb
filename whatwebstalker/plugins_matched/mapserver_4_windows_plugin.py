import sys
import os
			
class Pluginmapserver_4_windows_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<title>MS4W - MapServer 4 Windows</title>" },
			{ "version" : "/<h1>MS4W - MapServer 4 Windows - version ([^<]+)<\/h1>\s+<h2>Introduction<\/h2>/" },
		]

