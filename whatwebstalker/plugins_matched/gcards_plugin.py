import sys
import os
			
class Plugingcards_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<a href="compose.php?imageid=" },
			{ "text" : "<title>eCards Administration Console Login</title>" },
			{ "version" : "/<td>(Driftet av|Powered by|Un script de ) <a href="http:\/\/www.gregphoto.net\/gcards\/index.php"[^>]*>gCards<\/a> v([\d\.]+)<\/td>/", "offset" : "1 },
		]

