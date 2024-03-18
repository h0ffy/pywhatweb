import sys
import os
			
class powermta_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "status" : '403", "text" : '<html><body>Access denied.  Please consult the http-access directive in the User's Guide for more information.</body></html>" },
			{ "certainty" : '25", "search" : 'headers[www-authenticate]", "regexp" : '/^Basic realm="PowerMTA"$/ },
		]

