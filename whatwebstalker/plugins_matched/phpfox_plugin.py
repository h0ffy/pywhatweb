import sys
import os
			
class phpfox_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/Powered By <a href="http:\/\/www\.phpfox\.com\/"[^>]*>phpFoX<\/a> Version ([\d\.]+)/ }
			{ "version" : '/<a href="http:\/\/www\.phpfox\.com\/"[^>]*>Powered by phpFoX Version ([\d\.]+)<\/a>/ }
	]

