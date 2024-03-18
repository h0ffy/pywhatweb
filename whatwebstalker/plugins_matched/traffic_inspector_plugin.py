import sys
import os
			
class traffic_inspector_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Traffic [Ii]nspector HTTP\/FTP\/Proxy server \(([^\)]+)\)$/ },
			{ "url" : '/", "string" : /<title>Error<\/title><\/head><body><h1>403 - Forbidden<\/h1><hr( class="footer")?>Traffic [Ii]nspector HTTP\/FTP\/Proxy server \([^\)]+\)<br>([^<^\/]+)\s*\/?\s*[\d]{2}\.[\d]{2}\.[\d]{2}/", "offset" : '1 },
		]

