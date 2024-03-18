import sys
import os
			
class jobberbase_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'Companies Sitemap "Proudly powered by jobberBase"", "certainty" : '75 }
			{ "text" : '<meta name="author" content="http://www.jobberbase.com" />' }
			{ "regexp" : '/Proudly powered by[\s]+<a href="http:\/\/www.jobberbase.com\/"[^>]*title="open source job board software">jobberBase<\/a>/ }
	]

