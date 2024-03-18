import sys
import os
			
class Pluginw3_total_cache_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Performance optimized by W3 Total Cache. Learn more: http://www.w3-edge.com/wordpress-plugins/" },
		]
		return(self.rules)

