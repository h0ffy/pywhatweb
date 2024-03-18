import sys
import os
			
class apache_test_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>Test Page for Apache Installation</title>", "string" : 'Default" },
			{ "text" : '<TITLE>Test Page for the SSL/TLS-aware Apache Installation on Web Site</TITLE>", "string" : 'Default" },
			{ "text" : '<html><body><h1>It works!</h1></body></html>", "string" : 'Default" },
			{ "text" : '<html>Apache is functioning normally</html>", "string" : 'Default" },
			{ "text" : 'Apache is working on your cPanel<sup>&reg;</sup> and WHM&#8482; Server", "string" : 'Default" },
			{ "url" : '/icons/apache_pb.gif", "md5" : '48bc8b181b36c9289866a2e30f6afedd" },
			{ "url" : '/icons/apache_pb2.gif", "md5" : '36ccabeb1ad841c6af37660c3865a9c9", "version" : '2.x" },
			{ "url" : '/icons/apache_pb2.gif", "md5" : '726dac78d3a989a360fc405452a798ee", "version" : '2.2" },
			{ "regexp" : '/^Apache/i", "search" : 'headers[server]", "name" : 'HTTP Server Header"},
			{ "version" : '/^Apache\/([\d\.]+)/i", "search" : 'headers[server]", "name" : 'HTTP Server Header"},
			{ "certainty" : '75", "module" : 'mod_security", "regexp" : '/^NOYB$/", "search" : 'headers[server]"},
			{ "certainty" : '75", "name" : 'htacess WWW-Authenticate realm", "search" : 'headers[www-authenticate]", "regexp" : '/Basic realm="htaccess password prompt"},
		]

