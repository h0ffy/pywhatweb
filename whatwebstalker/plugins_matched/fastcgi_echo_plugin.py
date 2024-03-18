import sys
import os
			
class fastcgi_echo_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'SCRIPT_NAME=/fcgi-bin/echo' }
			{ "text" : '<title>FastCGI echo</title><h1>FastCGI echo</h1>' }
			{ "text" : 'REQUEST_URI=/fcgi-bin/echo' }
			{ "version" : '/HTTP_ORACLE_CACHE_VERSION=([\d\.]+)/ }
			{ "version" : '/SERVER_SOFTWARE=([^\n]+)/ }
			{ "version" : '/SERVER_SIGNATURE=<ADDRESS>([^<]+)/ }
		]

