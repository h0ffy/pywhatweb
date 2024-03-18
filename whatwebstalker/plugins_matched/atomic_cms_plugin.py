import sys
import os
			
class atomic_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by AtomicCms <a href="http://atomiccms.com/" target="_blank">content management' },
			{ "version" : '/Powered by AtomicCms ([\d\.]{1,15}) <a href="http:\/\/atomiccms.com\/" target="_blank">content management/ },
			{ "url" : 'favicon.ico", "md5" : '9f500a24ccbdda88cf8ae3ec7b61fc40" },
		]

