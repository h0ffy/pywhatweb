import sys
import os
			
class mediawiki_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'alt="Powered by MediaWiki"' },
			{ "certainty" : '75", "ghdb" : 'inurl:wiki MediaWiki' },
			{ "version" : '/<meta name="generator" content="MediaWiki ([^\s^"]+)" \/>/ },
			{ "version" : '/<td><a href="http:\/\/www\.mediawiki\.org\/" class="external text" rel="nofollow">MediaWiki<\/a><\/td>[\s]+<td>([^<]+)<\/td>/ },
		]

