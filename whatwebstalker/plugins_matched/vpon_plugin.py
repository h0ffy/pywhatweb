import sys
import os
			
class Pluginvpon_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/ctrl_ver.js", "version" : "/^var live_video_control_version ="([^"]+)";/" },
			{ "url" : "/ctrl_ver.js", "model" : "/^var vpon_platform = "([^"]+)";/" },
			{ "search" : "headers[server]", "version" : "/^VPON Server\/([\d\.]+)$/" },
		]
		return(self.rules)

