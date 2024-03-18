import sys
import os
			
class Pluginsdl_tridion_wcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[product-version]", "version" : "/^(.+)$/" },
			{ "search" : "headers[product]", "string" : /^Tridion (20[\d]{2}) Dynamic Content Web Application$/" },
		]

