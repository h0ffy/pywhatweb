import sys
import os
			
class redaxscript_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by <a href="http://redaxscript.com">Redaxscript</a>' },
			{ "version" : '/<meta name="generator" content="Redaxscript ([^\s^"]+)" \/>/ },
			{ "version" : '/Powered by <a href="http:\/\/redaxscript\.com" title="Redaxscript">Redaxscript<\/a> ([^\s^<]+)</ },
		]

