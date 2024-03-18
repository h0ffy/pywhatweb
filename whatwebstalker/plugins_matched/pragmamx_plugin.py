import sys
import os
			
class pragmamx_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- COPYRIGHT www.pragmamx.ca / Ne touchez pas / Do not touch -->' }
			{ "version" : '/<meta name="generator" content="pragmaMx ([^\s]+) - by http:\/\/pragmaMx\.org" \/>/ }
			{ "module" : /<!-- (pmx-templatesystem v[^\s^\/]+)\/20[\d]{2}-[\d]{2}-[\d]{2} -->/ }
			{ "version" : '/<p>Diese Webseite basiert auf pragmaMx ([^\s]+)\.<\/p>/ }
	]

