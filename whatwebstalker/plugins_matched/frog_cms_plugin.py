import sys
import os
			
class frog_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'poweredBy", "regexp" : '/(Powered by|Running|Propuls.{2} par)[^<]*<a href="http:\/\/www.madebyfrog.com\/"[^>]*>Frog CMS}
			{ "name" : 'default rss feed", "text" : '<link rel="alternate" type="application/rss+xml" title="Frog Default RSS Feed"'}
	]

