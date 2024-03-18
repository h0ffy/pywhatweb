import sys
import os
			
class Pluginbuddy_zone_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered By <a href="http://www.vastal.com" class="bottom">Buddy Zone</a>" },
		]
		return(self.rules)

