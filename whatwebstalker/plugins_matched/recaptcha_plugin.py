import sys
import os
			
class recaptcha_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<noscript>[\s]*<iframe src="http:\/\/www\.google\.com\/recaptcha\/api\/noscript\?k=/" },
		]

