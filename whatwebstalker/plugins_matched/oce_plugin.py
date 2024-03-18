import sys
import os
			
class Pluginoce_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>Print Exec Workgroup<\/title>/i },
			{ "text" : "/servlet/owslhtml/owslicons/header_pewg.jpg" },
		]
		return(self.rules)

