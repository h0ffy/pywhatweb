import sys
import os
			
class Pluginoracle_access_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<p id="footerVersion">Oracle Access Manager Version: ([^\s]+)<\/p>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/ObSSOCookie=[^;]+;/", "certainty" : "75 },
			{ "search" : "headers[location]", "regexp" : "/obrareq\.cgi/", "certainty" : "75 },
		]

