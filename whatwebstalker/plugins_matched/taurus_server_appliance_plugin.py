import sys
import os
			
class taurus_server_appliance_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "text" : '<title>The Taurus Server Appliance</title>' }
			{ "text" : '<b><font color=#FFFFFF>Welcome to Taurus </font></b>' }
			{ "version" : '/<div align=center><font size=-2 color=#FFFFFF>Software Version : CeLinuX-([\d\.]+)<\/font><\/div>/ }
	]

