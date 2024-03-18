import sys
import os
			
class Pluginbigace_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.bigace.de/" target="_blank">BIGACE</a>" },
			{ "version" : "/Powered by <a href="http:\/\/www.bigace.de\/"[^>]*>BIGACE ([\d\.]+)<\/a>/" },
			{ "version" : "/<meta name="generator" content="BIGACE ([\d\.]+)"( \/)?>/" },
			{ "version" : "/<!--[\r\n][\r\n]   Site is running BIGACE ([\d\.]+) [\r\n]        a PHP based Web CMS for MySQL[\r\n]             \(C\) Kevin Papst \(www.bigace.de\)[\r\n]/" },
		]

