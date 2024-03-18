import sys
import os
			
class obm_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "version" : '/<title>Login - OBM ([^\s^<]+)<\/title>/ }
			{ "regexp" : '/<body>[\s]+[\s]+<p id="aliasource">[\s]+<a href="http:\/\/www\.obm\.org">OBM\.org<\/a>[\s]+<\/p>[\s]+<h1>/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/OBM_Session=[\s]+;/ }
		]

