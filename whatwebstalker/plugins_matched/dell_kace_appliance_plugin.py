import sys
import os
			
class dell_kace_appliance_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : "/common/about.php", "version" : "/<b>K1000 Systems Management Appliance<\/b> <b>v([^\s^<]+)<\/b>/" },
			{ "search" : "headers[x-dellkace-version]", "version" : "/^(.+)$/" },
			{ "search" : "headers[x-dellkace-host]", "string" : /^(.+)$/" },
			{ "search" : "headers[x-dellkace-appliance]", "model" : "/^(.+)$/" },
			{ "search" : "headers[x-kbox-version]", "version" : "/^(.+)$/" },
			{ "search" : "headers[x-kbox-webserver]", "string" : /^(.+)$/" },
		]

