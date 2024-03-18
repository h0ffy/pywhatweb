import sys
import os
			
class Pluginexponent_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="Generator" content="Exponent Content Management System - ([^\"]+)"/" },
			{ "text" : "<meta name="Generator" content="Exponent Content Management System" },
			{ "text" : "Powered by <a href="http://www.exponentcms.org">Exponent CMS</a>" },
			{ "text" : "<a href="http://www.exponentcms.org">Powered by Exponent CMS</a>" },
		]
		return(self.rules)

