import sys
import os
			
class inout_adserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "function trim(stringValue){return stringValue.replace(/(^\s*|\s*$)/", "");}", "certainty" : "75 },
			{ "text" : "<title>Inout Adserver - Pay Per Click Advertising Expert!</title>" },
			{ "text" : "<title>Inout Search Engine Admin Login</title>" },
			{ "text" : "Powered by <a href="http://www.inoutscripts.com/?r=0">Inoutscripts</a>", "certainty" : "75 },
		]

