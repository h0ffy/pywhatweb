import sys
import os
			
class trac_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'Powered by Trac" +intitle:Trac", "certainty" : '75 }
			{ "version" : '/Powered by <a[^>]*><strong>Trac ([^<]+)<\/strong><\/a><br \/>/ }
	]

