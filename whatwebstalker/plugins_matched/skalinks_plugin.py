import sys
import os
			
class skalinks_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "Powered by <a class=sub_cat href="http://www.skalinks.com">SkaLinks - Link Exchange Script" },
			{ "text" : "Powered by <a class=sub_cat href="http://www.skalinks.com" rel="nofollow">SkaLinks - Link Exchange Script" },
			{ "text" : "Powered by <a class=sub_cat rel="nofollow" href="http://www.skalinks.com">SkaLinks - Link Exchange Script" },
		]

