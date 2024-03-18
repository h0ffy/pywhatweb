import sys
import os
			
class s_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<p class="alignRight">Powered by S:CMS - Copyright ©" },
			{ "text" : "<title>SCMS</title>" },
			{ "text" : "<!-- Inizio righe di indicizzazione nei motori di ricerca -->" },
			{ "version" : "/Powered by <a href='http:\/\/www.matteoiammarrone.com\/public\/s-cms' target='_blank'>S-Cms ([\d\.]+)<\/a>/" },
		]

