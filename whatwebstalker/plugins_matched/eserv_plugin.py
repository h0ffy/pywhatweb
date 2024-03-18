import sys
import os
			
class eserv_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Eserv\/([^\s]+)/ }
			{ "version" : '/<meta name="generator" content="Eserv\/([^\s^"]+)" \/>/ }
			{ "version" : '/<span id='powered_by'>[^<]+<a href="http:\/\/www\.eserv\.ru\/"><span itemprop="name">Eserv<\/span><\/a>\/([^\s]+)/ }
		]

