import sys
import os
			
class php_xmlrpc_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="XML-RPC for PHP" />' }
			{ "version" : '/<div class="footer">Generated using PHP-XMLRPC ([\d\.]+)<\/div>/ }
		]

