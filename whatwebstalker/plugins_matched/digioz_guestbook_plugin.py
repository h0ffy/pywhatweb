import sys
import os
			
class Plugindigioz_guestbook_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- NOTE: PLEASE DO NOT REMOVE THE BELLOW 3 LINES FROM YOUR HEADER FILE -->" },
			{ "text" : "<!-- NOTE: PLEASE DO NOT REMOVE THE ABOVE 3 LINES FROM YOUR HEADER FILE -->" },
			{ "version" : "/<title>Powered by DigiOz Guestbook Version ([\d\.]+)<\/title>/" },
			{ "version" : "/<a href="http:\/\/www\.digioz\.com"[^>]*>DigiOz (\.NET )?Guestbook Version ([\d\.]+)<br( \/)?>&copy; 20[\d]{2} DigiOz Multimedia\./", "offset" : "1 },
		]

