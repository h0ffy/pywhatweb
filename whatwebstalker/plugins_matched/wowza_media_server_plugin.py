import sys
import os
			
class wowza_media_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<html><head><title>Wowza Media Server [\d]+ Monthly Edition ([\d\.]+ build[\d]+)<\/title><\/head><body>Wowza Media Server [\d]+ Monthly Edition ([\d\.]+ build[\d]+)<\/body><\/html>/ }
			{ "search" : 'headers[www-authenticate]", "text" : 'realm="Wowza Media Systems"' }
		]

