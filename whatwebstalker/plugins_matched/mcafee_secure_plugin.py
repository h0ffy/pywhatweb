import sys
import os
			
class Pluginmcafee_secure_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<a target="?_blank"? href="https?:\/\/www\.(mcafeesecure|scanalert)\.com\/RatingVerify\?ref=([^"]+)"[^>]*>[\s]*<img/i", "offset" : "1 },
		]
		return(self.rules)

