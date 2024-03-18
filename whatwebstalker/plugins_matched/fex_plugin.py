import sys
import os
			
class fex_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/logo.jpg", "md5" : 'ad8a95bba8dd1a61d70bd38611bc2059" }
			{ "text" : '<HEAD><TITLE>F*EX - File EXchange</TITLE></HEAD>' }
			{ "certainty" : '75", "text" : '<h1>F*EX - Frams' Fast File EXchange" }
			{ "regexp" : '/<a href="mailto:[^"]+">fexmaster<\/a><\/address>/i }
			{ "search" : 'headers[server]", "regexp" : '/^fexsrv$/ }
		]

