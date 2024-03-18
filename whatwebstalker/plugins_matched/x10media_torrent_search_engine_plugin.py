import sys
import os
			
class Pluginx10media_torrent_search_engine_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "This search engine is in no way intended for illegal downloads.", "certainty" : "75 },
			{ "text" : "	<meta name="copyright" content="X10Media"/>", "certainty" : "75 },
			{ "text" : "	<meta name="contributor" content="X10Media"/>", "certainty" : "75 },
			{ "text" : "<title>Torrent Search Engine Script</title>" },
			{ "text" : "Powered by <a href="http://www.x10media.com/torrent-search-engine-script/" target="_blank">x10media Torrent Search Engine Script</a>" },
		]

