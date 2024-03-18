import sys
import os
			
class Pluginhttp_explorer_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Http explorer ([^\s]+)$/" },
			{ "version" : "/<p id="pgfooter_p_main">\s+<a href="http:\/\/http\-explorer\.sourceforge\.net\/\?lang=[^"]+">Http explorer\s+([^\s^<]+)<\/a>/" },
		]
		return(self.rules)

