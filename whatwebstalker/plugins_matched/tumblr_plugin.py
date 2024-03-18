import sys
import os
			
class Plugintumblr_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<link rel="(shortcut )?icon" href="http:\/\/[\d]{1,2}\.media\.tumblr\.com\/avatar_[a-f\d]{12}_16\.gif"[\s]?\/>/" },
			{ "regexp" : "/<meta name="tumblr-theme" content="[\d]+"[\s]?\/>/" },
			{ "text" : "<!-- BEGIN TUMBLR CODE --><iframe src="http://assets.tumblr.com/iframe.html" },
		]
		return(self.rules)

