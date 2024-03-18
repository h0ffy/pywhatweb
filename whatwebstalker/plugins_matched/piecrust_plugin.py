import sys
import os
			
class piecrust_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<meta name="generator" content="PieCrust" />" },
			{ "version" : "/<meta name="generator" content="PieCrust ([^\s^"]+)" \/>/" },
			{ "version" : "/Baked with <em><a href="http:\/\/bolt80\.com\/piecrust\/">PieCrust<\/a> ([^\s^<]+)<\/em>\.<\/p>/" },
		]

