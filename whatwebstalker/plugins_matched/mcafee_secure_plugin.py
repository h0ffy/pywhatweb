import sys
import os
			
class mcafee_secure_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<a target="?_blank"? href="https?:\/\/www\.(mcafeesecure|scanalert)\.com\/RatingVerify\?ref=([^"]+)"[^>]*>[\s]*<img/i", "offset" : "1 },
		]

