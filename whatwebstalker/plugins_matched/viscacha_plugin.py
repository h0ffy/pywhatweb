import sys
import os
			
class viscacha_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="Viscacha (http://www.viscacha.org)" />' }
			{ "text" : '<link rel="copyright" href="http://www.viscacha.org" />", "certainty" : '75 }
			{ "version" : '/Powered by <strong><a[^>]+href="http:\/\/www\.viscacha\.org" target="_blank">Viscacha ([^<]+)<\/a>/ }
	]

