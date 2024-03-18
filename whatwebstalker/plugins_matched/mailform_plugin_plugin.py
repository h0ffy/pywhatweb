import sys
import os
			
class mailform_plugin_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<a href="http:\/\/www.h-fj.com\/blog\/mtplgdoc\/mailformv[\d\.\_]+.php"[^>]*>Powered by Mailform plugin[s]? V([\d\.]+)<\/a>/i },
			{ "version" : "/<a href="http:\/\/www.h-fj.com\/blog\/mtplgdoc\/mailformv[\d\.\_]+.php"[^>]*>Powered by Mailform V([\d\.]+)<\/a>/i },
		]

