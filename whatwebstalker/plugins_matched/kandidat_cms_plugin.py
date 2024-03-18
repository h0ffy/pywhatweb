import sys
import os
			
class kandidat_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/Powered by[\ ]?[:]? <a href="http:\/\/www.kan-studio.ru[\/]?">Kandidat CMS<\/a>/ },
		]

