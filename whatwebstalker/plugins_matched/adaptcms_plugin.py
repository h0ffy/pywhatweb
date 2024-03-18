import sys
import os
			
class Pluginadaptcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/Powered by <a href="http:\/\/www.adaptcms.com">[<b>]*AdaptCMS([^<]*)<\/a>/" },
		]

