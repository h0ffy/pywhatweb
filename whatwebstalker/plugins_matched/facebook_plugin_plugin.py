import sys
import os
			
class Pluginfacebook_plugin_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "string" : /<i?frame[^>]+src[\s]*="http:\/\/(www|apps)\.facebook.com\/plugins\/([^\.^\/^\?]+)\.php\?/i", "offset" : "1 },
		]

