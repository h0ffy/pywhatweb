import sys
import os
			
class Pluginhycus_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="Hycus - Open Source PHP Based Content Management" />" },
			{ "text" : "Powered By <a href="http://www.hycus.com" target="_blank" >Hycus-CMS</a>. Developed By <a href="http://www.hycus.com" target="_blank" >Hycus Team</a>." },
		]

