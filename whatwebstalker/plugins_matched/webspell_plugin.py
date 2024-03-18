import sys
import os
			
class webspell_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="webSPELL" />' }
			{ "version" : '/This site is using the <a href="http:\/\/www.webspell.org" target="[^"]+">webSPELL (Free Content Management System|script) \(version: ([^\)]+)\)[\s]*<\/a>/", "offset" : '1 }
			{ "version" : '/Diese Seite benutzt das <a href="http:\/\/www.webspell.org" target="[^"]+">webSPELL Script \(Version: ([^\)]+)\)[\s]*<\/a>/ }
			{ "certainty" : '75", "search" : 'headers[set-cookie]", "regexp" : '/ws_session=[a-z\d]+;/ }
	]

