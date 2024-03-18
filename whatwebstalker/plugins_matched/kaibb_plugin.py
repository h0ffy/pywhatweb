import sys
import os
			
class kaibb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- THIS MUST REMAIN INTACT AND SHOWN ON ALL PAGES -->' }
			{ "version" : '/Powered by <a href="http:\/\/www\.kaibb\.co\.uk" class="normfont">KaiBB ([^\s^<]+)<\/a>/ }
			{ "version" : '/Powered by <a href="http:\/\/\www\.mi-dia\.co\.uk" class="normfont">KaiBB ([^\s^<]+)<\/a>/ }
			{ "text" : '<meta name="Description" http-equiv="Description" content="Forum powered by KaiBB - Powered by KaiBB" />' }
		]

