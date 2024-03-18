import sys
import os
			
class Pluginindices_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<!--[\s]+Pleasant Apache directory listings courtesy of Indices:[\s]+http:\/\/antisleep\.com\/software\/indices[\s]+-->/" },
			{ "version" : "/<div class="credits">[\s]+<a href="http:\/\/antisleep\.com\/software\/indices">Indices<\/a> ([^\s]+)[\s]+<\/div>/" },
		]
		return(self.rules)

