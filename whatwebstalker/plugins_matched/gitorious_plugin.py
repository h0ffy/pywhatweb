import sys
import os
			
class gitorious_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<a href="http:\/\/gitorious\.org"><img alt="Poweredby" src="\/images\/\.\.\/img\/poweredby\.png\?[\d]+" title="Powered by Gitorious" \/><\/a><\/div>/ },
			{ "search" : 'headers[set-cookie]", "regexp" : '/_gitorious_sess=[^-]+--[^;]+; domain=/ },
		]

