import sys
import os
			
class Pluginkandidat_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by[\ ]?[:]? <a href="http:\/\/www.kan-studio.ru[\/]?">Kandidat CMS<\/a>/" },
		]
		return(self.rules)

