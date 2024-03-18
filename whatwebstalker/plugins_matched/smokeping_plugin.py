import sys
import os
			
class Pluginsmokeping_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<tr><td class="menuitem" colspan="2">&nbsp;-&nbsp;<a class="menulink" HREF="?target=" },
			{ "version" : "/<A HREF="http:\/\/oss\.oetiker\.ch\/smokeping\/counter\.cgi\/([^\s\/\"]+)"><img border="0" src="[^"]+"><\/a>/" },
		]

