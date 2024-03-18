import sys
import os
			
class Pluginpragmamx_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- COPYRIGHT www.pragmamx.ca / Ne touchez pas / Do not touch -->" },
			{ "version" : "/<meta name="generator" content="pragmaMx ([^\s]+) - by http:\/\/pragmaMx\.org" \/>/" },
			{ "module" : /<!-- (pmx-templatesystem v[^\s^\/]+)\/20[\d]{2}-[\d]{2}-[\d]{2} -->/" },
			{ "version" : "/<p>Diese Webseite basiert auf pragmaMx ([^\s]+)\.<\/p>/" },
		]
		return(self.rules)

