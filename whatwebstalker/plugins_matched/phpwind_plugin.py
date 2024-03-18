import sys
import os
			
class Pluginphpwind_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "25", "regexp" : "/<title>[^<]+ - (powered by phpwind.net|Powered by PHPWind)<\/title>/" },
			{ "version" : "/<meta name="generator" content="PHPWind [v]?([^"^\(]+)(\([\d]+\))?" \/>/i },
			{ "text" : "Powered by <a href="http://www.phpwind.net/" target="_blank"><b>PHPWind</b></a>" },
			{ "version" : "/Powered by <a href="http:\/\/www.phpwind.net\/" target="_blank"><b>PHPWind<\/b><\/a>[\s]*<a href="http:\/\/www.phpwind.net\/" target="_blank"><b style="color:#FF9900">v([\d\.]+)<\/b><\/a>/" },
		]

