import sys
import os
			
class flyspray_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- Please don't remove this line - it helps promote Flyspray -->" },
			{ "text" : '<a href="http://flyspray.org/" class="offsite">Powered by Flyspray</a>' },
		]

