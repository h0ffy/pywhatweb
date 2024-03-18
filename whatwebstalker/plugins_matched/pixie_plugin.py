import sys
import os
			
class pixie_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/href="http:\/\/www.getpixie.co.uk" title="Get Pixie">(Pixie Powered|Powered by Pixie|Pixie)<\/a>/ },
			{ "version" : '/<meta name="generator" content="Pixie ([\d\.]+) - Copyright \(C\) [\d]{4} - [\d]{4}\." \/>/ },
		]

