import sys
import os
			
class Pluginobm_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "version" : "/<title>Login - OBM ([^\s^<]+)<\/title>/" },
			{ "regexp" : "/<body>[\s]+[\s]+<p id="aliasource">[\s]+<a href="http:\/\/www\.obm\.org">OBM\.org<\/a>[\s]+<\/p>[\s]+<h1>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/OBM_Session=[\s]+;/" },
		]
		return(self.rules)

