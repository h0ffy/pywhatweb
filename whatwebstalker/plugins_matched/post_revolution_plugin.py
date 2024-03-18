import sys
import os
			
class Pluginpost_revolution_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.postrev.com.ar/">Post Revolution</a>" },
		]
		return(self.rules)

