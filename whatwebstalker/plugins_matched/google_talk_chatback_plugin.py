import sys
import os
			
class google_talk_chatback_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<iframe[^>]+src[\s]*=[\s]*('|")http:\/\/www.google.com\/talk\/service\/badge\/Show\?tk=[^>]+>/" },
		]

