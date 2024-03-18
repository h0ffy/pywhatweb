import sys
import os
			
class phppgadmin_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'PPA_ID Cookie", "search" : 'headers[set-cookie]", "regexp" : '/^PPA_ID=[a-z0-9]+/ },
			{ "text" : '<td><span class="appname">phpPgAdmin</span></td>' },
			{ "version" : '%r{<span class="appname">phpPgAdmin</span> <span class="version">([\d\.]+)</span>} },
		]

