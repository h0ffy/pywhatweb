import sys
import os
			
class phorum_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/powered by <a href="http:\/\/www\.phorum\.org\/"( target="_blank")?>Phorum<\/a>\./ }
			{ "certainty" : '75", "text" : '<!-- end of div id=user-info -->' }
		]

