import sys
import os
			
class dedicated_micros_device_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : "/gui/title.shtml", "model" : "/^				var product = '([^']+)';[\s]*$/" },
			{ "url" : "/common/script_variables.js.shtml", "model" : "/^var SYSTEM_LOGO = "([^"]+)";[\s]*$/" },
			{ "url" : "/webpages/index.shtml", "text" : "	<title>DVIP</title>", "model" : "DVIP" },
			{ "search" : "headers[server]", "regexp" : "/^ADH-Web$/" },
		]

