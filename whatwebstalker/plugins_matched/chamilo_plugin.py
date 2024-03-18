import sys
import os
			
class chamilo_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-powered-by]", "version" : '/^Chamilo ([\d\.]+)/ },
			{ "text" : '<link href="http://www.chamilo.org/documentation.php" rel="Help" />' },
			{ "regexp" : '/<meta name="Generator" content="Chamilo ([\d\.]+)">/ },
			{ "text" : '<!-- end of #main" started at the end of banner.inc.php -->' },
			{ "version" : '/<\/div>(Portal|Plattform|Platform|Plataforma) <a href="http:\/\/www\.chamilo\.org\/?" target="_blank">Chamilo ([^<^\s]+)<\/a> &copy;/", "offset" : '1 },
			{ "version" : '/<div class="copyright">(Portal|Plattform|Platform|Plataforma) <a href="http:\/\/www\.chamilo\.org\/?" target="_blank">Chamilo ([^<^\s]+)<\/a> &copy;/", "offset" : '1 },
		]

