import sys
import os
			
class vbportal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="vbPortal - Copyright 2010" />' }
			{ "text" : '	<!-- Do not remove  or your scheduled tasks will cease to function -->' }
			{ "version" : '/<meta name="generator" content="vbPortal ([\d\.]+)" \/>/ }
			{ "version" : '/Portal By vbPortal Version ([\d\.]+)<br \/>/ }
	]

