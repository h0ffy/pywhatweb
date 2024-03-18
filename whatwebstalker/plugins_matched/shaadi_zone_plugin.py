import sys
import os
			
class Pluginshaadi_zone_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<a href='http://www.vastal.com/' target='_blank'>Powered By Shaadi Zone</a>." },
			{ "text" : "Powered By <a href='http://www.vastal.com/' target=\"_blank\">Shaadi Zone</a>" },
		]

