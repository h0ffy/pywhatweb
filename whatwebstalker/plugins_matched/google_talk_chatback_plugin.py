import sys
import os
			
class Plugingoogle_talk_chatback_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<iframe[^>]+src[\s]*=[\s]*('|")http:\/\/www.google.com\/talk\/service\/badge\/Show\?tk=[^>]+>/" },
		]
		return(self.rules)

