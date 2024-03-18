import sys
import os
			
class isp_config_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/powered by <a HREF="http:\/\/www.ispconfig.org">ISPConfig<\/a>/i }
			{ "certainty" : '75", "text" : 'This IP address is shared. For access to the web site which you look for", "enter its address instead of its IP.' }
		]

