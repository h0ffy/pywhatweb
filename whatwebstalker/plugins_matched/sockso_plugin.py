import sys
import os
			
class sockso_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Sockso$/ },
			{ "version" : '/<p id="legal">[\s]+<strong>Sockso<\/strong>[\s]+v([^<]+)<br \/>[\s]+&copy; 20[\d]{2}/ },
		]

