import sys
import os
			
class Pluginphp_shell_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "+filetype:php +HAXPLORER +"Server Files Browser" +Browsing +"Script Location"", "certainty" : "75 },
			{ "version" : "/PHPShell by [a-zA-Z0-9]+ - Version ([0-9a-z\.]+)/" },
		]
		return(self.rules)

