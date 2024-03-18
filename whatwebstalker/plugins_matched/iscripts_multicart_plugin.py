import sys
import os
			
class Pluginiscripts_multicart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/Powered by <a href="http:\/\/iscripts.com\/multicart"[\ target="_blank"]*><font color="#[a-zA-Z0-9]{6}"><b>iScripts Multicart<\/b><\/font><\/a>. A premium product from <a href="http:\/\/www.iscripts.com" class=" target="_blank"><font color="#[a-zA-Z0-9]{6}"><b>iScripts.com<\/b><\/font><\/a><\/div>/" },
		]

