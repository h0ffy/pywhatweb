import sys
import os
			
class elxis_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by <a href="http://www.elxis.org" title="Elxis CMS">Elxis</a>' },
			{ "regexp" : '/Powered by <a href="http:\/\/www.elxis.org[\/]*" title="Elxis open source content management system"[\ target="_blank"]*>Elxis[\ CMS]*<\/a>/ },
			{ "regexp" : '/<meta name="Generator" content="Elxis - Copyright \(C\) 2006-[0-9]{4} Elxis.org. All rights reserved." \/>/ },
			{ "md5" : '36d8efa82de41f53c23eece784405c9e", "url" : 'images/favicon.ico' },
		]

