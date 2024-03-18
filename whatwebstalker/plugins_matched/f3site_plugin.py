import sys
import os
			
class f3site_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<a href="http://compmaster.prv.pl" target="_blank">powered by F3Site</a></span>' },
			{ "regexp" : '/Powered by[^>]*<a[^>]*href="http:\/\/compmaster.prv.pl[^>]*>F3Site[^>]*<\/a>/ },
			{ "regexp" : '/Powered by[^>]*<a[^>]*href="http:\/\/dhost.info\/compmaste[^>]*>F3Site[^<]*<\/a>/ },
			{ "version" : '/Powered by <a href="http:\/\/compmaster.prv.pl">F3Site v([\d\.]+) plus<\/a>/ },
		]

