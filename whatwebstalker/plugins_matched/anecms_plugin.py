import sys
import os
			
class anecms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="Author" content="Erwin Aligam - ealigam@gmail.com" />' }
			{ "ghdb" : 'powered by anecms"", "certainty" : '75 }
			{ "regexp" : '/&copy; [\d]{4} <strong><a href="http:\/\/anecms.com[^\>]*>anecms.com<\/a><\/strong>/ }
			{ "regexp" : '/<title>[^<^\-]+- Powered By ANECMS<\/title>/ }
		]

