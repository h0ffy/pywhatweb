import sys
import os
			
class speedtouch_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : "/favicon.ico", "md5" : "befcded36aec1e59ea624582fcb3225c" },
			{ "regexp" : "/(Basic|Digest) realm="SpeedTouch/", "search" : "headers[www-authenticate]", "name" : "WWW-Authenticate realm" },
		]

