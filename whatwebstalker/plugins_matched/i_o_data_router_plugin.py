import sys
import os
			
class Plugini_o_data_router_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/", "model" : "/<title>I-O DATA Wireless Broadband Router (WN-[^\s^<]+)<\/title>/" },
		]
		return(self.rules)

