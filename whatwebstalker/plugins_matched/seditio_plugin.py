import sys
import os
			
class seditio_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="Seditio by Neocrome http://www.neocrome.net" />' },
			{ "text" : '<a href="http://www.neocrome.net">Powered by Seditio</a><br />' },
			{ "text" : '<br />Powered by <a href="http://www.neocrome.net" target="_blank">Seditio</a>' },
		]

