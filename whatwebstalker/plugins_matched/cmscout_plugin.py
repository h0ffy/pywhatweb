import sys
import os
			
class cmscout_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/Powered by CMScout &copy;[\d\,]+ <a href="http:\/\/www.cmscout.za.net" title="CMScout Group" target="_blank">CMScout Group<\/a>/ }
			{ "text" : '<!--Shows the CMScout and website copyright information. Please do not remove this without permission from the CMScout admin-->' }
	]

