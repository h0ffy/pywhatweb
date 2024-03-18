import sys
import os
			
class dugallery_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'ext:asp inurl:DUgallery intitle:"3.0"", "version" : '3.0", "certainty" : '75 },
			{ "regexp" : '/<title>DUgallery[^<]*<\/title>/ },
			{ "text" : '<img src="assets/title.gif" alt="Powered by DUportal" width="269" height="62" border="0">' },
			{ "version" : '/<title>DUgallery ([\d\.]+)<\/title>/ },
		]

