import sys
import os
			
class Pluginloggix_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="Loggix" />" },
			{ "version" : "/Powered by <a href="http:\/\/loggix.gotdns.org">Loggix<\/a> ver.([\d\.]+)<\/address>/" },
		]

