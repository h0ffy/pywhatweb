import sys
import os
			
class Pluginmyshell_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "&nbsp;| ::::::::::&nbsp;<a href="http://www.digitart.net" target="_blank" style="text-decoration:none"><b>MyShell</b> &copy;2001 Digitart Producciones</a>" },
			{ "version" : "/<title>MyShell ([\d\.]+ build [\d]{8})<\/title>/" },
		]

