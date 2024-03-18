import sys
import os
			
class Pluginclearwell_e_discovery_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/esa/", "text" : "/><a class="needHelp" style="text-decoration:none" href="javascript:logonHelp();void(0);">Need help?</a>" },
			{ "url" : "/esa/", "text" : "<title>Clearwell E-Discovery Platform log in</title>" },
		]
		return(self.rules)

