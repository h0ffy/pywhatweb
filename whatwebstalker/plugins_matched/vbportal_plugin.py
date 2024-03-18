import sys
import os
			
class Pluginvbportal_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="vbPortal - Copyright 2010" />" },
			{ "text" : "	<!-- Do not remove  or your scheduled tasks will cease to function -->" },
			{ "version" : "/<meta name="generator" content="vbPortal ([\d\.]+)" \/>/" },
			{ "version" : "/Portal By vbPortal Version ([\d\.]+)<br \/>/" },
		]
		return(self.rules)

