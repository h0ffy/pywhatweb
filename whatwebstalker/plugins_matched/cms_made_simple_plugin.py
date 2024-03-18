import sys
import os
			
class Plugincms_made_simple_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "name" : "CMSSESSID cookie", "regexp" : "/^CMSSESSID/", "search" : "headers[set-cookie]" },
			{ "name" : "Meta generator", "text" : "<meta name="Generator" content="CMS Made Simple" },
			{ "name" : "Powered by footer", "version" : "/This site is powered by <a[^>]+>CMS Made Simple<\/a> version ([0-9\.]+)/" },
			{ "name" : "Admin Login Title", "text" : "<title>Login to CMS Made Simple</title>", "url" :  "/admin/login.php" },
			{ "name" : "Version from /doc/CHANGELOG.txt", "version" : "/^Version ([^ ]+).*/m", "url" : "/doc/CHANGELOG.txt" },
			{ "name" : "favicon", "url" : "/favicon_cms.ico", "md5" : "ebf500d206705bda0cb79021c15da98a" },
		]

