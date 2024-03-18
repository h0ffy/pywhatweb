import sys
import os
			
class iguard_security_system_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '	<TITLE>iGuard Fingerprint Security System</TITLE>' }
			{ "firmware" : '/	<meta content="Lucky-Tech iGuard ([\d\.]{1,5})" name="GENERATOR">/ }
			{ "url" : '/Admins/Content.vtml", "firmware" : '/iGuard Security[^<]+<\/td><\/tr><tr><td>Firmware Version<\/td><td>([^<]+)<\/td>/ }
			{ "url" : '/Admins/Content.vtml", "string" : /<tr><td>Registered Automatch<\/td><td>([^<]+)<\/td><\/tr>/ }
	]

