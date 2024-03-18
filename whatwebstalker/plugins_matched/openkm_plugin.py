import sys
import os
			
class openkm_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<form name="login" method="post" action="j_security_check" onsubmit="setCookie()">' }
			{ "regexp" : '/<title>OpenKM Login<\/title>[\s]+<\/head>[\s]+<body onload="document\.forms\[0\]\.elements\[0\]\.focus\(\)">/ }
		]

