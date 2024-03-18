import sys
import os
			
class php_csl_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="description" content="PHP Code Snippet Library stores all your code for you for easy access", "runs on any PHP platform and does not require a database... easy to install and full of features.">' },
			{ "text" : '<!-- Please note the credit message below is required if you want support -->' },
			{ "version" : '/<td align="right" class="hdr">Powered by: <a href="http:\/\/www\.php-csl\.com\/" class="foot" title="PHP-CSL">PHP-CSL V([^<]+)<\/a>&nbsp;<\/td>/ },
		]

