import sys
import os
			
class Pluginxmb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- Powered by XMB " },
			{ "text" : "<!-- The XMB Group -->" },
		]

