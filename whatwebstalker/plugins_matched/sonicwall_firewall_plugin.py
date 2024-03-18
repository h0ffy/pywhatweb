import sys
import os
			
class sonicwall_firewall_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^SonicWALL$/ }
			{ "url" : '/auth1.html", "module" : /<div align="right">Click <a href="sslvpn" onClick="top\.location\.href='sslvpn'";>here<\/a> for (sslvpn) login/ }
			{ "url" : '/auth1.html", "firmware" : '/<link href="swl_login-([^"]+)\.css" rel="stylesheet" type="text\/css">/ }
		]

