import sys
import os
			
class artiphp_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<!--  fin ArtiMenu horizontal -->" },
			{ "text" : "<!--  Fin ArtiMenu horizontal -->" },
			{ "text" : "<!-- copyright Artiphp", "merci de respecter notre travail en laissant notre signature -->" },
			{ "version" : "/<div id="copyright">\s*(<p class="copyright">)?\s*<a href="http:\/\/www\.(artiphp|artiloo)\.com"( target="_blank")?>Artiphp ([^<]+)<\/a> &copy; 2001-20[\d]{2} est un logiciel libre/", "offset" : "3 },
		]

