import sys
import os
			
class openwrt_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<title>OpenWrt Administrative Console</title>" },
			{ "text" : "OpenWrt Administrative Console<br />Redirecting to : <a style="color: inherit;" href="/cgi-bin/webif.sh">main page</a></p>" },
		]

