import sys
import os
			
class werkzeug_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Werkzeug\/([\d\.]+)/ },
			{ "status" : '302", "certainty" : '75", "text" : '<p>You should be redirected automatically to target URL:' },
		]

