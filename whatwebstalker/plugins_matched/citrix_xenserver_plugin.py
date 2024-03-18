import sys
import os
			
class citrix_xenserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/", "version" : '/<html>\s+<title>XenServer ([^\s^<]+)<\/title>\s+<head>\s+<\/head>\s+<body>\s+<p\/>Citrix Systems", "Inc\. XenServer ([^\s]+)\s+<p\/><a href="XenCenter\.iso">XenCenter CD image<\/a>\s+<p\/><a href="XenCenter\.msi">XenCenter installer<\/a>/ },
			{ "url" : '/", "md5" : '141c8bbcda4cf773763e9f2108d62ff3" },
		]

