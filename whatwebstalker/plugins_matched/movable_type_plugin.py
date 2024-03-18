import sys
import os
			
class movable_type_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'meta generator tag", "regexp" : '/<meta name="generator" content="http:\/\/www\.movabletype\.org\/" \/>},
			{ "text" : '<title>Movable Type System Check [mt-check.cgi]</title>' },
			{ "version" : '/<li><strong>Movable Type version:<\/strong> <code>([^<]+)<\/code><\/li>/ },
			{ "filepath" : '/<li><strong>Current working directory:<\/strong> <code>([^<]+)<\/code><\/li>/ },
			{ "name" : 'Powered by link", "regexp" : '/<a href="http:\/\/sixapart\.com">Powered by Movable Type<\/a>},
			{ "name" : 'Powered by link", "regexp" : '/Powered by <a href="http:\/\/www\.movabletype\.com\/"[^>]*>Movable Type<\/a>/ },
		]

