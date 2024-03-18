import sys
import os
			
class Pluginsonicwall_ssl_vpn_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^SonicWALL SSL-VPN Web Server\.?$/" },
		]
		return(self.rules)

