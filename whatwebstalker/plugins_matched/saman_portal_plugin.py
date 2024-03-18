import sys
import os
			
class saman_portal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<meta name="Generator" content="Saman Information Structure" />" },
			{ "version" : "/<script  type="text\/javascript" language="JavaScript" src="\/portlets\/sisRapid\/dream\/libs\/(V[\d\.]+)\/core\/sisValidationAPI\.js">/" },
			{ "regexp" : "/<script  type="text\/javascript" language="JavaScript">[\s]+var sisTHEMEPATH_HTTP = "/" },
			{ "search" : "headers[server]", "regexp" : "/sisRapid Framework/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/SAMANPORTALSID=[^;]+;/" },
		]

