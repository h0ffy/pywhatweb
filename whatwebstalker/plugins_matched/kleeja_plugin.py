import sys
import os
			
class kleeja_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<title>[^\(]+\(Powered by Kleeja\)<\/title>/ },
			{ "text" : '<meta name="copyrights" content="Powered by Kleeja :: kleeja.com" />' },
			{ "text" : '<meta name="Description" content="Powered by Kleeja :: kleeja.com" />' },
			{ "text" : 'Powered by <a href="http://www.kleeja.com/" target="_blank">Kleeja</a>' },
			{ "text" : '<!-- IF REMOVE: Pay for a license -->' },
			{ "text" : '<!-- IF REMOVE: Pay for a license - see http://www.kleeja.com -->' },
		]

