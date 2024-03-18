import sys
import os
			
class Pluginzte_iad_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "search" : "headers[server]", "version" : "/^Mini web server ([^\s]+) ZTE corp 20[\d]{2}\.$/" },
			{ "model" : "I532", "url" : "/image/banner_I532.jpg", "md5" : "b7b298d358d9c0ae59224a1c3d3c5585" },
			{ "model" : "I202", "url" : "/image/I202.gif", "md5" : "68b697d421f07bf16f27ac0d44410f05" },
			{ "model" : "ZXV10 I508C", "url" : "/image/banner_top.jpg", "md5" : "b968f243974f9e97b8a9e71bfaa25c83" },
		]
		return(self.rules)

