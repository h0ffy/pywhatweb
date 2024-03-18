import sys
import os
			
class Pluginwebsvn_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link rel="alternate" type="application/rss+xml" title="WebSVN RSS" href="rss.php?repname=" },
			{ "text" : "<link rel='alternate' type='application/rss+xml' title='WebSVN RSS' href='rss.php?repname=" },
			{ "md5" : "beb816a701a4cee3c2f586171458ceec", "url" : "templates/BlueGrey/images/favicon.ico" },
			{ "md5" : "b2bb1d54c7bab453c0e054b31b6919e4", "url" : "templates/BlueGrey/images/websvn.png" },
		]
		return(self.rules)

