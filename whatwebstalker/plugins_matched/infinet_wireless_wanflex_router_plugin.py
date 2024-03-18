import sys
import os
			
class infinet_wireless_wanflex_router_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<meta name="generator" content="InfiNet Wireless Company" />" },
			{ "search" : "headers[server]", "version" : "/^WANFlex HTTP Daemon v([^\s]+)$/" },
		]

