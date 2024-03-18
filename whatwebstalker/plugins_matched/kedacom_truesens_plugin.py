import sys
import os
			
class kedacom_truesens_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "regexp" : "/^KEDACOM-Webs$/" },
			{ "url" : "/index.htm", "text" : "<body><span style="font:12px;">Loading...</span></body>" },
			{ "text" : "<img src="./img/kedacom-logo.jpg" alt="WEB CONSOLE" /></td>" },
		]

