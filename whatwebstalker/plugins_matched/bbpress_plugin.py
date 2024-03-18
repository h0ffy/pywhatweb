import sys
import os
			
class bbpress_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="generator" content="bbPress ([\d\.]+)" \/>/ },
			{ "regexp" : '/ is proudly powered by <a[^>]+href="http:\/\/bbpress\.org">bbPress<\/a>/ },
			{ "text" : '<!-- If you like showing off the fact that your server rocks -->' },
			{ "text" : '<div id="bbpress-forums">' },
		]

