import sys
import os
			
class mcafee_epolicy_orchestrator_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<title>\s+ePolicy Orchestrator ([^\s]+ \(Build: \d+\))\s+<\/title>/ },
			{ "url" : '/EPOCore/images/epo-logo-login.gif", "md5" : 'aa4beb20b354c761257271e86e9ec92b", "version" : '4.x" },
			{ "search" : 'headers[server]", "regexp" : '/^Undefined$/ },
		]

