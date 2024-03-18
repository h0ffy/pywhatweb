import sys
import os
			
class pagecookery_microblog_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/Powered by <a href="http:\/\/pagecookery.com\/" target="_blank">PageCookery<\/a> Microblog ([\d\.]{1,5})/" },
		]

