import sys
import os
			
class httpfileserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div id=footer>[\s]+<a href="http:\/\/www\.rejetto\.com\/hfs\/">HttpFileServer ([^<]+)<\/a>[\s]+<br \/>Servertime/ }
			{ "version" : '/^HFS (\d\.\d.+)$/", "search" : 'headers[server]" }
			{ "regexp" : '/^HFS /", "search" : 'headers[server]" }
	]

