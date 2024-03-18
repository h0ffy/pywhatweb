import sys
import os
			
class Pluginbuddy_zone_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered By <a href="http://www.vastal.com" class="bottom">Buddy Zone</a>" },
		]

