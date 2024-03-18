import sys
import os
			
class cgiproxy_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'filetype:cgi "Start browsing through this CGI-based proxy by entering a URL below"", "certainty" : '75 }
			{ "text" : '<title>Start Using CGIProxy</title>' }
			{ "version" : '/<a href="http:\/\/www.jmarshall.com\/tools\/cgiproxy\/"><i>CGIProxy ([^<]+)<\/i><\/a>/ }
	]
