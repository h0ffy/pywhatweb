import sys
import os
			
class Pluginscrutinizer_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div id='testAlertDivTitle'>Scrutinizer ([^<]+)<\/div>/" },
			{ "regexp" : "/<link id='scrutStyle' rel="stylesheet" href="\/css\/classic\.css/" },
			{ "regexp" : "/<div id='testAlertHdrMsg'>For the best Scrutinizer experience possible", "please address the issues below:<\/div>/" },
		]
		return(self.rules)

