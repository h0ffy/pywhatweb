import sys
import os
			
class pluck_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'powered by pluck" +admin inurl:"file=kop1.php"' }
			{ "version" : '/<meta name="generator" content="pluck ([^\s^"]+)" \/>/ }
			{ "text" : 'powered by <a href="http://www.pluck-cms.org">pluck</a>' }
	]

