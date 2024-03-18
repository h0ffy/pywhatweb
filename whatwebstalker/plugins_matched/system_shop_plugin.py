import sys
import os
			
class Pluginsystem_shop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "      powered by System4you.com internet solutions" },
			{ "text" : "                powered by System-Shop" },
			{ "text" : "               http://www.system-shop.at" },
			{ "text" : "<a href="http://www.systemshop.at" target="_blank">Powered by System" },
		]

