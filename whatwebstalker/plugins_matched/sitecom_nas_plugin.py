import sys
import os
			
class Pluginsitecom_nas_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "search" : "headers[www-authenticate]", "text" : "Basic realm="SITECOM LOGIN Enter Password (default is sitecom)" },
		]
		return(self.rules)

