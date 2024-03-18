import sys
import os
			
class Pluginkedacom_truesens_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^KEDACOM-Webs$/" },
			{ "url" : "/index.htm", "text" : "<body><span style="font:12px;">Loading...</span></body>" },
			{ "text" : "<img src="./img/kedacom-logo.jpg" alt="WEB CONSOLE" /></td>" },
		]
		return(self.rules)

