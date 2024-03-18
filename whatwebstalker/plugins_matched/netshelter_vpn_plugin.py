import sys
import os
			
class Pluginnetshelter_vpn_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<HEAD><TITLE>Welcome to NetShelter</TITLE></HEAD>" },
			{ "url" : "/images/sb_logo.gif", "md5" : "ffacfeae7e203bd8de5c9da889d217ec" },
			{ "search" : "headers[server]", "regexp" : "/^NetShelter\/VPN$/" },
		]

