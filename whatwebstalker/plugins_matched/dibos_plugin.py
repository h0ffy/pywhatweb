import sys
import os
			
class dibos_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<title>DiBos - Login<\/title>/i },
			{ "text" : "<link rel="STYLESHEET" type="text/css" href="style/bovisnt.css"></link>" },
			{ "text" : "<h2>Object moved to <a href="/Error.aspx?error=wrongbrowser">here</a>.</h2>'},
		]

