import sys
import os
			
class Plugincisco_ace_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "url" : "/favicon.ico", "md5" : "5ee29688a968d3912880b3780cdde42e" },
			{ "text" : "<link href="/utility/cuesStylesLogo.css" rel="stylesheet" type="text/css" />" },
			{ "version" : "/<div class="cuesLoginVersionInfo">Version ([^\s]+)<\/div>/" },
			{ "model" : "/<div class="cuesLoginProductName">ACE ([^\s]+) Device Manager<\/div>/" },
		]
		return(self.rules)

