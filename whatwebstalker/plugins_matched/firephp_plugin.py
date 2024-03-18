import sys
import os
			
class firephp_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-wf-1-plugin-1]", "version" : '/^http:\/\/meta\.firephp\.org\/Wildfire\/Plugin\/FirePHP\/Library-FirePHPCore\/([^\s]+)$/ }
			{ "search" : 'headers[x-wf-1-structure-1]", "string" : /^http:\/\/meta\.firephp\.org\/Wildfire\/Structure\/FirePHP\/(FirebugConsole\/[^\s]+)$/ }
			{ "search" : 'headers[x-wf-protocol-1]", "regexp" : '/^http:\/\/meta\.wildfirehq\.org\/Protocol\// }
	]

