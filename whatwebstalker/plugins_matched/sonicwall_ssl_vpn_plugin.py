import sys
import os
			
class Pluginsonicwall_ssl_vpn_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^SonicWALL SSL-VPN Web Server\.?$/" },
		]

