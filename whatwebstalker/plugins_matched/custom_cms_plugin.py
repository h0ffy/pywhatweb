import sys
import os
			
class custom_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : ' - Powered by CCMS</title>", "certainty" : '75 },
			{ "text" : '<meta name="generator" content="CustomCMS Gaming" />' },
			{ "version" : '/power.png" border="0" style="margin-top: 7px;" alt=" title="Powered by CCMS v([\d\.]+)" \/><\/a>/ },
		]

