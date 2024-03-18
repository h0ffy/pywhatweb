import sys
import os
			
class aardvark_topsites_php_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : "Powered by Aardvark Topsites PHP"" },
			{ "regexp" : "/Powered by <a href="http:\/\/www.aardvarktopsitesphp.com[^>]*>[^A]*Aardvark Topsites PHP/i },
			{ "version" : "/Powered by <a href="http:\/\/www.aardvarktopsitesphp.com\/"><b>Aardvark Topsites PHP<\/b><\/a> ([\d\.]+)/" },
			{ "version" : "/Powered by <a href="http:\/\/www.aardvarkind.com\/">Aardvark Topsites PHP<\/a> ([\d\.]+)/" },
		]

