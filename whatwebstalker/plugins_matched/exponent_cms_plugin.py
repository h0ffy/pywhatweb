import sys
import os
			
class exponent_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<meta name="Generator" content="Exponent Content Management System - ([^\"]+)"/" },
			{ "text" : "<meta name="Generator" content="Exponent Content Management System" },
			{ "text" : "Powered by <a href="http://www.exponentcms.org">Exponent CMS</a>" },
			{ "text" : "<a href="http://www.exponentcms.org">Powered by Exponent CMS</a>" },
		]

