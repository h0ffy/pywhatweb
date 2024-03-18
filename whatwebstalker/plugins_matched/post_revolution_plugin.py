import sys
import os
			
class Pluginpost_revolution_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.postrev.com.ar/">Post Revolution</a>" },
		]

