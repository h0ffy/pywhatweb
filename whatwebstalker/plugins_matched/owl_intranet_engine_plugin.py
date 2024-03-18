import sys
import os
			
class owl_intranet_engine_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[set-cookie]", "regexp" : "/owl_sessid=/" },
			{ "version" : "/<a class="version2" href="http:\/\/owl\.sourceforge\.net\/" target="_blank">Owl Intranet Engine", "Version Owl ([^<]+)<\/a>/" },
			{ "version" : "/<title>[^<]+ Owl ([\d\.]+ [\d]{8})<\/title>/" },
		]

