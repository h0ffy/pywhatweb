import sys
import os
			
class oracle_fusion_middleware_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>Welcome to Oracle Fusion Middleware</title>' },
			{ "text" : '<link href="css/fmw_bottom_area.css" rel="stylesheet" type="text/css">' },
			{ "version" : '/<div id="welcome_text">TO ORACLE<strong> FUSION MIDDLEWARE ([^\s^<]+)<\/strong> <\/div>/ },
			{ "search" : 'headers[server]", "regexp" : '/^Oracle-Fusion-Middleware/ },
			{ "search" : 'headers[server]", "version" : '/^Oracle-Fusion-Middleware\/([^\s]+ \([^\)]+\))/ },
		]

