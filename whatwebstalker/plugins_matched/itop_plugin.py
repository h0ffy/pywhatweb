import sys
import os
			
class itop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<p><b>Error</b>: Unable to read the configuration file: 'config-itop.php'. Please check the access rights on this file.</p>" },
			{ "text" : '<p><b>Security Warning</b>: the configuration file 'config-itop.php' should be read-only.</p><p>Please modify the access rights to this file.</p>" },
			{ "text" : '<title>iTop Login</title>' },
			{ "version" : '/<div id="login-logo"><a href="http:\/\/www\.combodo\.com\/itop"><img title="iTop [^\s]+ ([^\s^"]+)" src="\.\.\/images\/itop-logo/ },
		]

