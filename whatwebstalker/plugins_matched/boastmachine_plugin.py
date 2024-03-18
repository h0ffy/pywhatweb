import sys
import os
			
class boastmachine_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'powered by boastMachine" +"Recent posts"", "certainty" : '75 }
			{ "version" : '/Powered by <a href="http:\/\/boastology.com">boastMachine v([\d\.]+)<\/a>/ }
			{ "regexp" : '/<a href="http:\/\/boastology.com"><img src="http:\/\/[^>]*alt="Powered by boastMachine" \/><\/a>/ }
	]

