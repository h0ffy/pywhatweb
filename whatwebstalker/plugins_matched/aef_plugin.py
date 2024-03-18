import sys
import os
			
class aef_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "text" : '<meta name="keywords" content="aef", "advanced", "electron", "forum", "bulletin", "board", "software" />' }
			{ "version" : '/<a href="http:\/\/www\.anelectron\.com">Powered By AEF ([^<]{1,256})<\/a> &copy; [\d]{4}/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/AEFCookies[\d]*\[aefsid\]=/ }
		]

