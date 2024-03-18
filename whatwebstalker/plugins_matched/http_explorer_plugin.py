import sys
import os
			
class http_explorer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Http explorer ([^\s]+)$/ },
			{ "version" : '/<p id="pgfooter_p_main">\s+<a href="http:\/\/http\-explorer\.sourceforge\.net\/\?lang=[^"]+">Http explorer\s+([^\s^<]+)<\/a>/ },
		]

