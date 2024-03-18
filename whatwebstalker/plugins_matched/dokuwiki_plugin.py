import sys
import os
			
class dokuwiki_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'powered by DokuWiki" inurl:doku.php filetype:php' }
			{ "regexp" : '/<div class="dokuwiki"[\s]?>/ }
			{ "text" : '<meta name="generator" content="DokuWiki" />' }
			{ "version" : '/<meta name="generator" content="DokuWiki Release ([^"]+)" \/>/ }
		]

