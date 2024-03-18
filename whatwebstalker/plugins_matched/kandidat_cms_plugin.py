import sys
import os
			
class Pluginkandidat_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/Powered by[\ ]?[:]? <a href="http:\/\/www.kan-studio.ru[\/]?">Kandidat CMS<\/a>/" },
		]

