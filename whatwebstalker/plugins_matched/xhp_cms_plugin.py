import sys
import os
			
class xhp_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>XHP installation</title>' },
			{ "version" : '/<meta name="GENERATOR" content="XHP - eXpandable Home Page v([\d\.]+)"\/>/ },
			{ "version" : '/<a href="http:\/\/xhp.targetit.ro\/">Powered by XHP CMS v([\d\.]+)<\/a><br\/><a href="http:\/\/lars.targetit.ro\/">Site engine is copyright/ },
		]

