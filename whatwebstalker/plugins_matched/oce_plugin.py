import sys
import os
			
class oce_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<title>Print Exec Workgroup<\/title>/i },
			{ "text" : '/servlet/owslhtml/owslicons/header_pewg.jpg' },
		]

