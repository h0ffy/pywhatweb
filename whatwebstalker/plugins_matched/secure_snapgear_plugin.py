import sys
import os
			
class secure_snapgear_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/img/logo.ico", "md5" : 'a27c392bc74b2d5c0e10fa7c1132c74d" }
			{ "model" : '/<td class="menu"><div class="logo"><a href="\/cgi-bin\/cgix\/default"><img class="logo" alt="([^"]+)" src="\/img\/logo\.gif"><\/a>/ }
			{ "string" : /<html><head><title>([^\s]+)\nManagement Console<\/title>/ }
			{ "string" : /<html><head><title>([^\s]+) - SnapGear Management Console\n<\/title>/ }
		]

