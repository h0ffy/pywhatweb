import sys
import os
			
class axous_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<meta name="generator" content="Axous V([^"]+)" \/>/ }
			{ "version" : '/Powered by <a href="http:\/\/www\.axous\.com\/" target="_blank" title="Axous Shareware Shop">Axous ([^\s]+)<\/a> &copy;/ }
			{ "text" : '<div class="tit2 tit3">Products</div>' }
	]

