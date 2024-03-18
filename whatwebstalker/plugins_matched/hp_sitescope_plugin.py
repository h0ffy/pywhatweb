import sys
import os
			
class hp_sitescope_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<center><H2>SiteScope Login</H2></center><hr>' },
			{ "url" : '/", "version" : '/<p class=fine align=center><small>SiteScope ([\d\.]+)/ },
		]

