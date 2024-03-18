import sys
import os
			
class Pluginnewswall_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<div id="screen"><noscript><p class="js">\s*There's no newswall without javascript - please activate\.\.\.\s*<\/p><\/noscript><\/div>/" },
		]
		return(self.rules)

