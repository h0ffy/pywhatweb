import sys
import os
			
class pressflow_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<a href="http:\/\/drupal.org"><img src="[\/a-zA-Z0-9\-\_+]*\/misc\/powered-blue-80x15.png" alt="Powered by Pressflow", "an open source content management system" title="Powered by Pressflow", "an open source content management system" width="80" height="15" \/><\/a>/ }
			{ "text" : '<title>Drupal already installed | Pressflow</title>", "version" : 'Install Page" }
		]

