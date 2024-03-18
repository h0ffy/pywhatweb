import sys
import os
			
class Pluginlpse_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[location]", "regexp" : "/^(https?:\/\/[^\/]+)?\/eproc\/app/" },
			{ "text" : "<link rel="stylesheet" type="text/css" href="/eproc/assets/application.css"/>" },
		]

