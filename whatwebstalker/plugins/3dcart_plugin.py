import sys
import os
			
class 3dcart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<!--START: 3dcart stats-->" },
			{ "text" : "<!--END: 3dcart stats-->" },
			{ "search" : "headers[set-cookie]", "regexp" : "/3dvisit/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/^affiliate\s/", "name" : "affiliate cookie", "certainty" : "25 },
		]

