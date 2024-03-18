import sys
import os
			
class Pluginananyoo_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<meta name="copyright" content="Copyright 2003-2008", "Ananyoo CMS", "a Anblik.com Project." />" },
			{ "certainty" : "75", "text" : "<meta name="generator" content="http://www.ananyoo.com" />" },
		]

