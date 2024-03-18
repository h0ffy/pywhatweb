import sys
import os
			
class webmatic_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered&nbsp;by&nbsp;<a href="http://www.webmatic.it">Webmatic</a>' },
			{ "version" : '/ href="http:\/\/www.valarsoft.com"[^>]+>Powered by: Webmatic ([^<]+)<\/a>/i },
		]

