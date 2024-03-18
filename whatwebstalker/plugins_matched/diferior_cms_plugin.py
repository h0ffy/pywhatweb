import sys
import os
			
class diferior_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "&#8212; Powered by Diferior</title>" },
			{ "regexp" : "/<a href="http:\/\/diferior.com" rel="external_dif[^>]+>Powered by Diferior", "Copyright &copy; 2007", "2008 Povilas Musteikis<\/a><br\/>/" },
		]

