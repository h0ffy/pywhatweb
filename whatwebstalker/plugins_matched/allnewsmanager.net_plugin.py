import sys
import os
			
class allnewsmanager.net_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/(kujeme|Powered by) <a id="[^"]+" href="http:\/\/www.allnewsmanager.net">AllNewsManager.NET<\/a>/ }
		]

