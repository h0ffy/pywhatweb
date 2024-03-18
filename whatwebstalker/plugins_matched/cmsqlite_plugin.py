import sys
import os
			
class cmsqlite_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div id="cmsqliteFooter"><span id="anchorFooter"><a href="http://www.cmsqlite.net" target="_blank">powered by CMSQLite</a></span></div></body></html>' },
			{ "text" : '<meta name="generator" content="www.CMSQLite.net by www.Netzabdruck.de" />' },
		]

