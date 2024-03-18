import sys
import os
			
class calypso_ion_8r_device_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "75", "text" : "<title>Calypso ION-8r Device</title>" },
			{ "text" : "<li><a href="/A/cfg/entercmd.stm">Enter Command</a></li>" },
			{ "search" : "headers[www-authenticate]", "text" : "Calypso ION8r Device" },
		]

