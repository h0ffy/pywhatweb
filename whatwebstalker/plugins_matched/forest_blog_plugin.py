import sys
import os
			
class forest_blog_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/Powered [B|b]?y[:]? <a href="http:\/\/www.hostforest.co.uk\/[^"]*"[^>]+title="Forest Blog"[^>]*>/ },
			{ "text" : '<title>Forest Blog Administration</title>' },
			{ "text" : '			<h1>Forest Blog Administration</h1>' },
			{ "version" : '/Powered [B|b]?y[:]? <a href="http:\/\/www.hostforest.co.uk\/[^"]*"[^>]+title="Forest Blog"[^>]*>Forest Blog<\/a> v([\d\.]+)/ },
		]

