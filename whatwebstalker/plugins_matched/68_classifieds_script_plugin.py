import sys
import os
			
class 68_classifieds_script_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "Powered by <a href="http://www.68classifieds.com">68 Classifieds Script</a>" },
			{ "version" : "/<meta name="author" content="68 Classifieds - v([^"]+)" \/>/" },
		]

