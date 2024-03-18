import sys
import os
			
class Pluginnewscoop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/newscoop\.sourcefabric\.org\/" target="_blank">\s+Newscoop<\/a>&nbsp;([\d\.]+)[^,]*,\s+the open content management system for professional journalists\./" },
			{ "text" : "Powered by Newscoop", "the open content management system for professional journalists.<br />" },
			{ "text" : "Powered by <a href="http://newscoop.sourcefabric.org/" target="_blank">Newscoop</a>", "the open content management system for professional journalists." },
			{ "text" : "<meta name="generator" content="Newscoop" />" },
		]

