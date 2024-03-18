import sys
import os
			
class Plugincgiproxy_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "filetype:cgi "Start browsing through this CGI-based proxy by entering a URL below"", "certainty" : "75 },
			{ "text" : "<title>Start Using CGIProxy</title>" },
			{ "version" : "/<a href="http:\/\/www.jmarshall.com\/tools\/cgiproxy\/"><i>CGIProxy ([^<]+)<\/i><\/a>/" },
		]
		return(self.rules)

