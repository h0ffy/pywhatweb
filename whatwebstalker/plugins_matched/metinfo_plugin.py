import sys
import os
			
class metinfo_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<meta name="copyright" content="Copyright 2008-20[\d]{2} MetInfo">/ }
			{ "regexp" : '/<meta name="author" content="[^"]+--Powered by MetInfo">/ }
			{ "version" : '/Powered by <a href="http:\/\/www.MetInfo.cn" target="_blank" title="MetInfo enterprise website manager system"><b>[^<]+<\/b><\/a> ([\d\.]+)/ }
		]

