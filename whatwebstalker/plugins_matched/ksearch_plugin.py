import sys
import os
			
class Pluginksearch_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "Powered by KSearch" inurl:ksearch.cgi filetype:cgi" },
			{ "version" : "/Powered by[\s]+<a[^>]+href="http:\/\/www\.kscripts\.com\/(scripts\.html#ksearch)?"[^>]*>KSearch[\s]+([\d\.]+[a-z]?)[\s]*<\/a>/", "offset" : "1 },
			{ "regexp" : "/Powered by[\s]+<a[^>]+href="http:\/\/www\.kscripts\.com\/(scripts\.html#ksearch)?"[^>]*>KSearch<\/a>/" },
		]
		return(self.rules)

