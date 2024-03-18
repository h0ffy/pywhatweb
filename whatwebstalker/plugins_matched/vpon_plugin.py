import sys
import os
			
class vpon_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : "/ctrl_ver.js", "version" : "/^var live_video_control_version ="([^"]+)";/" },
			{ "url" : "/ctrl_ver.js", "model" : "/^var vpon_platform = "([^"]+)";/" },
			{ "search" : "headers[server]", "version" : "/^VPON Server\/([\d\.]+)$/" },
		]

