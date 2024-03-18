import sys
import os
			
class php_update_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by <a href="http://www.php-update.co.uk" target="_blank">PHP-Update</a>' },
			{ "regexp" : '/Powered by <a href=[^>]*http:\/\/www.php-update.co.uk[^>]*>PHP[\ \-]*Update<\/a>/ },
			{ "regexp" : '/>Powered by PHP-Update<\/a>/i },
			{ "text" : '<a href="http://www.php-update.co.uk">Powered by PHP-Update </a>' },
		]

