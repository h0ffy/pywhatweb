import sys
import os
			
class Pluginpagecookery_microblog_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by <a href="http:\/\/pagecookery.com\/" target="_blank">PageCookery<\/a> Microblog ([\d\.]{1,5})/" },
		]
		return(self.rules)

