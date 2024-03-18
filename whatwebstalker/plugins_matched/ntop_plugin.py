import sys
import os
			
class ntop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^ntop\/([^\s]+)/ }
			{ "text" : '<link rel="alternate" type="application/rss+xml" title="ntop RSS Feed" href="http://www.ntop.org/blog/?feed=rss2" />' }
			{ "certainty" : '75", "text" : '<TITLE>Global Traffic Statistics</TITLE>' }
			{ "search" : 'headers[www-authenticate]", "text" : 'Basic realm="NTOP"' }
	]

