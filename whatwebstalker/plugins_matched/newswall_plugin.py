import sys
import os
			
class newswall_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<div id="screen"><noscript><p class="js">\s*There's no newswall without javascript - please activate\.\.\.\s*<\/p><\/noscript><\/div>/ },
		]

