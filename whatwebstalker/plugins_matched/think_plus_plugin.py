import sys
import os
			
class Pluginthink_plus_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div class="copy">Powered by <a href="http://think-plus.gr">Think+</a>" },
			{ "text" : "<meta name="author" CONTENT="Think+">" },
		]
		return(self.rules)

