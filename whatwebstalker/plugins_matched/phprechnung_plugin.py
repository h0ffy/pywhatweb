import sys
import os
			
class phprechnung_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<a class='slink' title='phpInvoice Home' href='http://www.ecorak.de/phpRechnung/' target='_blank'>" },
			{ "version" : "/<title>phpRechnung ([^-]+) - Login<\/title>/" },
			{ "version" : "/<title>phpInvoice ([^-]+) - Login<\/title>/" },
		]

