import sys
import os
			
class php_shell_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : '+filetype:php +HAXPLORER +"Server Files Browser" +Browsing +"Script Location"", "certainty" : '75 },
			{ "version" : '/PHPShell by [a-zA-Z0-9]+ - Version ([0-9a-z\.]+)/ },
		]

