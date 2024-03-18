import sys
import os
			
class Pluginfrog_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "poweredBy", "regexp" : "/(Powered by|Running|Propuls.{2} par)[^<]*<a href="http:\/\/www.madebyfrog.com\/"[^>]*>Frog CMS},
			{ "name" : "default rss feed", "text" : "<link rel="alternate" type="application/rss+xml" title="Frog Default RSS Feed"'},
		]
		return(self.rules)

