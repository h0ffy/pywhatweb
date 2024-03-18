import sys
import os
			
class interred_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<meta name="(generator|GENERATOR)" content="InterRed V([^,]+)", "http:\/\/www\.interred\.de\/", "InterRed GmbH"( \/)?>/", "offset" : "1 },
			{ "version" : "/<!-- Created with InterRed V([^,]+)", "http:\/\/www\.interred\.de\/", "by InterRed GmbH -->/" },
		]

