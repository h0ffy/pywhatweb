import sys
import os
			
class Pluginweb2project_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>web2Project Development :: web2Project Login</title>" },
			{ "text" : "</head><body>Fatal Error. You haven't created a config file yet.<br/><a href=" },
			{ "certainty" : "25", "version" : "/<meta name="Version" content="([^"^\s]+)" \/>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/web2project=[^;]+;/" },
		]
		return(self.rules)

