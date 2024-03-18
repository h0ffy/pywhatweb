import sys
import os
			
class Pluginrecaptcha_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<noscript>[\s]*<iframe src="http:\/\/www\.google\.com\/recaptcha\/api\/noscript\?k=/" },
		]
		return(self.rules)

