import sys
import os
			
class Pluginibm_websphere_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^WebSphere Application Server\/([^\s]+)$/" },
			{ "text" : "<HTML><HEAD><TITLE>Snoop Servlet</TITLE></HEAD><BODY BGCOLOR="#FFFFEE">", "module" : "Snoop Servlet" },
		]

