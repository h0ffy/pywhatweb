import sys
import os
			
class Pluginhivemail_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Database Error in HiveMail&trade;</title>" },
			{ "version" : "/\/\/ myaccounts holds the userpics\s+myaccounts = '[^']*';\s+recaptcha_global = "[^"]+";\s+hiveversion = "v([^"]+)";/" },
			{ "text" : "<input type="text" class="validate[ajax[ajaxUserCall]] input" name="answer" id="answer" />" },
			{ "version" : "/<meta name="product" content="Hivemail v([^"]+)">/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/hivesession=/" },
		]
		return(self.rules)

