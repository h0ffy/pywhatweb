import sys
import os
			
class cisco_adaptive_security_appliance_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<title>Cisco Systems", "Inc. Network Access</title>", "certainty" : "75 },
			{ "search" : "headers[server]", "regexp" : "/^Adaptive Security Appliance HTTP\/1\.1$/" },
			{ "regexp" : "/<FORM ACTION="\/netaccess\/redirect\.html">\s+<INPUT type=hidden name=sid VALUE=/" },
		]

