import sys
import os
			
class Pluginauto_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href="http://www.ventics.com/autocms/" target="_self">Powered by Auto CMS</a>,<a href="http://validator.w3.org/check?uri=referer">Valid XHTML 1.0</a>" },
		]
		return(self.rules)

