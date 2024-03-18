import sys
import os
			
class xoops_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "text" : '<!-- RMV: added module header -->' }
			{ "text" : '<meta name="generator" content="XOOPS" />' }
			{ "text" : '<meta name="author" content="XOOPS" />' }
			{ "regexp" : '/Powered by XOOPS [^\s]+ 2001-20[\d]{2} <a href="http:\/\/(xoops\.sourceforge\.net|www\.xoops\.org\/)"/ }
			{ "version" : '/Powered by XOOPS ([^\s]+) [^\s]+ 2001-20[\d]{2} <a href="http:\/\/(xoops\.sourceforge\.net|www\.xoops\.org\/)"/ }
		]

