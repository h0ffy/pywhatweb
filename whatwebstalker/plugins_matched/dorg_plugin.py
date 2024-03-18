import sys
import os
			
class dorg_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<p>Powered by <a href="http://www.discorganizer.org">DORG</a>" },
			{ "text" : "<title>DORG - Disc Organization System</title>" },
			{ "text" : "<title>DORG - admin panel</title>" },
			{ "text" : "<meta name="description" content="this is the administration panel of the DORG system" />" },
		]

