import sys
import os
			
class smodcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="Generator" content="SmodCMS" />' }
			{ "text" : '<meta name="Authoring_Tool" content="SmodCMS // www.smod.pl" />' }
			{ "regexp" : '/[P|p]+owered by <a href="http:\/\/www.smod.pl[\/]+"[^>]+>SmodCMS[\s]*<\/a>/ }
		]

