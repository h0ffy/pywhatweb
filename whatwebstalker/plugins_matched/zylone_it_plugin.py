import sys
import os
			
class zylone_it_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/Powered by[:]? <a href="http:\/\/www.zylone.com[\/]*[^>]+>Zylone IT/ },
		]

