import sys
import os
			
class enigma2_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<\?xml version="1\.0" encoding="UTF-8"\?>[\s]+<rss version="2\.0">[\s]+<channel>[\s]+<title>Enigma2 Movielist<\/title>/ }
			{ "text" : '<html><head><title>Enigma2 WebControl</title></head><body><h1>404 - Page not found</h1></body></html>' }
			{ "url" : '/web-data/img/favicon.ico", "md5" : 'd9aa63661d742d5f7c7300d02ac18d69" }
			{ "text" : '<link rel="alternate" type="application/rss+xml" title="Movie List" href="/web/movielist.rss?tag" >' }
		]

