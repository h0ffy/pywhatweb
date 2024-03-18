import sys
import os
			
class Pluginthink_plus_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<div class="copy">Powered by <a href="http://think-plus.gr">Think+</a>" },
			{ "text" : "<meta name="author" CONTENT="Think+">" },
		]

