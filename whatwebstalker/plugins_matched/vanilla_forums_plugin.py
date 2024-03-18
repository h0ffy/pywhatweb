import sys
import os
			
class vanilla_forums_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-garden-version]", "version" : '/^Vanilla ([^\s]+)$/ }
			{ "version" : '/Powered by <a href="(http:\/\/)?getvanilla\.com\/?">Vanilla ([^\s^<]+)<\/a>/", "offset" : '1 }
			{ "search" : 'headers[set-cookie]", "regexp" : '/Vanilla=deleted; expires=/ }
			{ "certainty" : '25", "regexp" : '/<body id=["'](DiscussionsPage|vanilla)/i }
		]

