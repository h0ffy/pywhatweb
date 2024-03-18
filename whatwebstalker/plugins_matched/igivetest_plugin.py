import sys
import os
			
class igivetest_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/Powered by <a href="http:\/\/iGiveTest\.com" target=_blank>iGiveTest v([\d\.]+)<\/a>/ }
			{ "version" : '/<tr><td colspan=[\d] align=right>Powered by iGiveTest v([\d\.]+)<\/a><\/td><\/tr>/ }
			{ "certainty" : '25", "text" : '<form action="index.php" method=post name=signinform>' }
		]

