import sys
import os
			
class duclassified_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "ghdb" : 'powered by DUclassified" intitle:DUclassified' },
			{ "name" : 'default title", "regexp" : '/<title>DUclassified[\s\d\.]*<\/title>},
			{ "name" : 'assets/DUclassified.css", "regexp" : '/<link[^>]href="[^"]*assets\/DUclassified.css"[^>]+>/ },
		]

