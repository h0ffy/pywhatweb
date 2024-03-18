import sys
import os
			
class oracle_http_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/Oracle[ -]HTTP[ -]Server/ },
			{ "search" : 'headers[server]", "version" : '/Oracle_Web_[Ll]istener(_NT_)?([\d\.]+\/[^\s]+)/", "offset" : '1 },
			{ "search" : 'headers[server]", "version" : '/Oracle_Web_[Ll]istener(_NT_)?\/([^\s]+)/", "offset" : '1 },
		]

