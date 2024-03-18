import sys
import os
			
class Pluginncr_itran_3000t_imaging_transport_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<html><title>Infinity Site Configuration<\/title>\s+<body bgcolor=white link=blue text=black vlink=maroon>\s+<center>\s+<p align=right>Version: ([^\s^<]+)<\/p>/" },
			{ "version" : "/<html>\s+<title>Main Menu<\/title>\s+<body bgcolor=white link=blue text=black vlink=maroon>\s+<p align=right>Version: ([^\s^<]+)<\/p>/" },
			{ "string" : /<h1><i><font color=red>Infinity<\/font><\/i> Main Menu<\/h1>\s+<b>([^<]+)<\/b>/" },
			{ "url" : "/setup.php", "account" : "/<input type=hidden name=setupItem\[\] value="\$cpassword"><input type=hidden name=setupTitle\[\] value="iSite Controller Password"><input name=setupValue\[\] value="([^\"^>]+)" size=40><\/td><\/tr>/" },
		]
		return(self.rules)

